from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()


model = ChatAnthropic(model="claude-2")  # Specify the model you want to use
response = model.invoke("What is the capital of France?")

print(response.content)  # Print the content of the response