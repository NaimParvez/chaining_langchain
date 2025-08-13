from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenAI(model="gemini-1.5-flash")  # Specify the model you want to use
response = model.invoke("What is the capital of Bangladesh?")

print(response.content)  # Print the content of the response