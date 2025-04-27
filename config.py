import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
WOLFRAM_ALPHA_APP_ID = os.getenv('WOLFRAM_ALPHA_APP_ID')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Email Configuration
EMAIL = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')