def serve_chai(flavour):
    try:
        print(f"preparing {flavour} chai")
        if(flavour == "unknown"):
            raise ValueError("Unknown flavour")
    except ValueError as e:
        print(f"Error: {e}")

    else:
        print(f"{flavour} chai is ready")
    finally:
        print("Thank you for visiting our chai shop")    




serve_chai("ginger")
serve_chai("unknown")