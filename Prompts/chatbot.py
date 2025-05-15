from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

model = ChatOpenAI(
    model="gpt-4o")

chat_history = [
    SystemMessage(
        content="You are a helpful ai Assistant. Answer the user question in a concise and informative manner."
    )
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    
    if user_input.lower() == "exit":
        break
    
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    
    # print(response.content)
    print(f"Chatbot: {response.content}")
    
print(f"Chat history:{chat_history}")