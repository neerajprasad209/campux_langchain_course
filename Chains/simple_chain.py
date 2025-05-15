from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {input} in a list format. ",
    input_variables=['input'],
    )

model = ChatOpenAI(model='gpt-4o')

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"input": "the Great Wall of China"})
print(result)