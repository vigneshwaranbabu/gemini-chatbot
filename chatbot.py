import os
import google.generativeai as genai
from dotenv import load_dotenv
import base64

# Load environment variables from .env file
load_dotenv()

# Decode the base64 encoded API key
encoded_api_key = os.getenv("GEMINI_API_KEY")
if encoded_api_key:
    decoded_api_key = base64.b64decode(encoded_api_key).decode("utf-8")
else:
    decoded_api_key = None

# Configure the API key from environment variable
try:
  genai.configure(api_key=decoded_api_key)
except AttributeError:
  print("Error: GEMINI_API_KEY not found in environment variables.")
  exit()

#Creating the model
model = genai.GenerativeModel("gemini-2.5-pro")

#Starting the chat session
chat = model.start_chat(history=[])
print("Chatbot is ready! Type 'exit' or 'quit' to end the session.")
print("="*50)

while True:
  user_input = input("You: ")
  if not user_input.strip():
    print("Please enter a valid message.")
    continue
  if user_input.lower() in ["exit", "quit"]:
    print("Ending the chat session. Goodbye!")
    break
  
  try:
    response = chat.send_message(user_input, stream=True)

    print("Chatbot: ", end="")
    for chunk in response:
      print(chunk.text, end="", flush=True)
    print("\n")
  except Exception as e:
    print(f"An error occurred: {e}")
    print("\n")