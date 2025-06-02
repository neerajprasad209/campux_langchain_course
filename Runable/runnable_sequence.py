from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain_core.output_parsers import StrOutputParser


from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a tweet about {topic}. ",
    input_variables=['topic'],
)

prompt2 = PromptTemplate(
    template="Explain the Following tweet: {tweet}. ",
    input_variables=['tweet'],
)

model = ChatOpenAI(model='gpt-4o')

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result = chain.invoke({"topic": "Machine Learning in Healthcare"})

print(result)