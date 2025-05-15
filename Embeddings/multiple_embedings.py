# text-embedding-3-large
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=32
    )

doc = [
    "What is Machine Learning?", 
    "What is Deep Learning?", 
    "What is Reinforcement Learning?"
    ]


result = embedding.embed_documents(doc)

print(result)