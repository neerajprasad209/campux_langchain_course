from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model ="gpt-4o")

messages = [
    (
        "system",
        "You are a helpful translator. Translate the user sentence to French.",
    ),
    ("human", "I love programming."),
]

result = llm.invoke(messages)

print(result.content)
