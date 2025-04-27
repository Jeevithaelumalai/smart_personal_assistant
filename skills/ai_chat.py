import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def chat_with_ai(prompt):
    """Generates AI response using OpenAI"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Sorry, I'm having trouble connecting to the AI service. Error: {str(e)}"