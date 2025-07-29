from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

model=ChatOpenAI(model="gpt-3.5-turbo-instruct") #temparatue=0-2 refers to the randomness of the output
# max_tokens=1000 refers to the maximum number of tokens in the output
response=model.invoke("What is the capital of France?")

print(response.content) 
