from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not api_key:
    raise EnvironmentError("API key not found. Make sure you set HUGGINGFACEHUB_API_TOKEN in .env")

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of Bangladesh?")
print(response.content)
