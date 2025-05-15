from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")


messages = [
    SystemMessage(
        content="You are a helpful ai Assistant. Answer the user question in a concise and informative manner."
    ),
    HumanMessage(content="What is the Tokenization?"),
]

result = llm.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)