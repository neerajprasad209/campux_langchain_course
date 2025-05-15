from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o')


prompt_1 = PromptTemplate(
    template="Generate a detailed report on the following topic: {input}. ",
    input_variables=['input'],)

prompt_2 = PromptTemplate(
    template="Summarize the following report into 5 points: {input}. ",
    input_variables=['input'],)

parser = StrOutputParser()

chain = prompt_1 | model | parser | prompt_2 | model | parser

result = chain.invoke({"input": "Machine Learning in Healthcare"})

print(result)

chain.get_graph().print_ascii()