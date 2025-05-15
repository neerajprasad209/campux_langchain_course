from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.5, max_output_tokens=20)

result = llm.invoke("What is machine learning?")
print(result.content)