import wolframalpha
from config import WOLFRAM_ALPHA_APP_ID

client = wolframalpha.Client(WOLFRAM_ALPHA_APP_ID)

def calculate(expression):
    """Performs calculations using Wolfram Alpha"""
    try:
        res = client.query(expression)
        return next(res.results).text
    except Exception as e:
        return f"Sorry, I couldn't calculate that. Error: {str(e)}"