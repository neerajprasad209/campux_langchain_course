from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate   
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Summarize the following text: {text}. ",
    input_variables=['text'],
)

loader = PyPDFLoader("./Document_Loaders/dl-curriculum.pdf")

documents = loader.load()

# chain = prompt | model | parser

# result = chain.invoke({"text": documents[0].page_content})

# print(result)

# print(documents)
print(len(documents))
print(documents[0].page_content)
print(documents[1].metadata)
