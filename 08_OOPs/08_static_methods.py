class ChaiUtils:
    @staticmethod
    def clean_ingredient(text):
        return [item.strip() for item in text.split(",")]
    

raw = "milk, sugar, tea, leaves, cardamom"  

obj = ChaiUtils()
cleaned = ChaiUtils.clean_ingredient(raw)

print(cleaned)  
