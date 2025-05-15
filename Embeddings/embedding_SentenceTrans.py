#sentence-transformers/all-MiniLM-L6-v2
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "What is Machine Learning?"

result = embedding.embed_query(text)

print(result)
