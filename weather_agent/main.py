import json
import os
import urllib.error
import urllib.parse
import urllib.request

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


def fetch_json(url, params):
    query = urllib.parse.urlencode(params)
    request_url = f"{url}?{query}"

    with urllib.request.urlopen(request_url, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def find_location(location_name):
    data = fetch_json(
        GEOCODING_URL,
        {
            "name": location_name,
            "count": 1,
            "language": "en",
            "format": "json",
        },
    )

    results = data.get("results", [])
    if not results:
        raise ValueError(f"No location found for '{location_name}'.")

    location = results[0]
    return {
        "name": location["name"],
        "country": location.get("country", ""),
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "timezone": location.get("timezone", "auto"),
    }


def fetch_forecast(location):
    return fetch_json(
        FORECAST_URL,
        {
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m",
            "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,wind_speed_10m_max",
            "forecast_days": 5,
            "timezone": location["timezone"],
        },
    )


def describe_weather(code):
    return WEATHER_CODES.get(code, f"Weather code {code}")


def build_forecast_report(location, forecast):
    current = forecast["current"]
    current_units = forecast["current_units"]
    daily = forecast["daily"]
    daily_units = forecast["daily_units"]

    lines = [
        f"Weather forecast for {location['name']}, {location['country']}".strip(),
        "",
        "Current conditions:",
        f"- Temperature: {current['temperature_2m']}{current_units['temperature_2m']}",
        f"- Feels like: {current['apparent_temperature']}{current_units['apparent_temperature']}",
        f"- Humidity: {current['relative_humidity_2m']}{current_units['relative_humidity_2m']}",
        f"- Wind: {current['wind_speed_10m']} {current_units['wind_speed_10m']}",
        f"- Conditions: {describe_weather(current['weather_code'])}",
        "",
        "5-day outlook:",
    ]

    for index, date in enumerate(daily["time"]):
        high = daily["temperature_2m_max"][index]
        low = daily["temperature_2m_min"][index]
        rain_chance = daily["precipitation_probability_max"][index]
        wind = daily["wind_speed_10m_max"][index]
        conditions = describe_weather(daily["weather_code"][index])

        lines.append(
            f"- {date}: {conditions}, high {high}{daily_units['temperature_2m_max']}, "
            f"low {low}{daily_units['temperature_2m_min']}, rain chance {rain_chance}%, "
            f"wind up to {wind} {daily_units['wind_speed_10m_max']}"
        )

    return "\n".join(lines)


def summarize_with_openai(user_question, forecast_report):
    if not os.getenv("OPENAI_API_KEY"):
        return None

    client = OpenAI()
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o"),
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a careful weather assistant. Use only the provided "
                    "forecast data. Do not invent exact values or conditions."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"User question: {user_question}\n\n"
                    f"Forecast data:\n{forecast_report}\n\n"
                    "Give a short, practical forecast summary and mention any "
                    "rain, heat, cold, or wind concerns."
                ),
            },
        ],
    )

    return response.choices[0].message.content


def main():
    user_query = input("Which location should I forecast? ")

    try:
        location = find_location(user_query)
        forecast = fetch_forecast(location)
        forecast_report = build_forecast_report(location, forecast)
    except urllib.error.URLError as error:
        print(f"Could not reach the weather service: {error}")
        return
    except (KeyError, ValueError) as error:
        print(f"Could not prepare forecast: {error}")
        return
    except Exception as error:
        print(f"Unexpected error: {error}")
        return

    summary = None
    try:
        summary = summarize_with_openai(user_query, forecast_report)
    except Exception as error:
        print(f"AI summary unavailable: {error}")

    print()
    if summary:
        print("AI summary:")
        print(summary)
        print("\nRaw forecast data:")
    else:
        print("Forecast:")

    print(forecast_report)


if __name__ == "__main__":
    main()
