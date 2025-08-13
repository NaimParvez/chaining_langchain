from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "the capital of France is Paris",
    "the capital of Bangladesh is Dhaka",
    "the capital of India is New Delhi",
]

result = embedding.embed_documents(documents)

print(str(result))