from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def main():
    user_query = input("Ask me anything about the weather: ")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_query}
        ],
    )

    print(f"Response: {response.choices[0].message.content}")


if __name__ == "__main__":
    main()