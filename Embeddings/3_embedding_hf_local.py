from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "the capital of France is Paris",
    "the capital of Bangladesh is Dhaka",
    "the capital of India is New Delhi",
]

vector = embedding.embed_documents(documents)

print(str(vector))