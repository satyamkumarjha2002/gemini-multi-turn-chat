import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable in your .env file")

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    print(f"Error configuring Gemini API: {str(e)}")
    exit(1)

temperature = 0.7
history = []

def get_user_input():
    return input("You: ").strip()

def get_model_response(prompt):
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(temperature=temperature)
        )
        return response.text
    except Exception as e:
        print(f"Error getting response from Gemini: {str(e)}")
        return None

def main():
    # First interaction
    user_input1 = get_user_input()
    history.append({"role": "user", "parts": [user_input1]})
    
    response1 = get_model_response(history)
    if response1:
        history.append({"role": "model", "parts": [response1]})
        print("\nGemini:", response1)
    
    # Second interaction
    user_input2 = get_user_input()
    history.append({"role": "user", "parts": [user_input2]})
    
    response2 = get_model_response(history)
    if response2:
        print("\nGemini:", response2)

if __name__ == "__main__":
    main()