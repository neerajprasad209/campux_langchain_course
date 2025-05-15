from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=32
    )

doc = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "Who is Jasprit Bumrah?"

doc_embeddings = embedding.embed_documents(doc)

# print("Document Embeddings:", doc_embeddings)

query_embedding = embedding.embed_query(query)

# print("Query Embedding:", query_embedding)
similarity_scores = cosine_similarity([query_embedding], doc_embeddings)

print("Similarity Scores:", similarity_scores[0])





