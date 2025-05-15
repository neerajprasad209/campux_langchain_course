from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation"
)

chat = ChatHuggingFace(llm=llm, verbose=True)

messages = [
        ("human", "What is Machine Learning?"),
]

output = chat.invoke(messages)

print(output.content)