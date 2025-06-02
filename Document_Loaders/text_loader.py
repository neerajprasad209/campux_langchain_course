from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o')

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Summarize the following text: {text}. ",
    input_variables=['text'],
)

loader = TextLoader("./Document_Loaders/cricket.txt", encoding="utf-8")

documents = loader.load()

chain = prompt | model | parser

result = chain.invoke({"text": documents[0].page_content})

print(result)

