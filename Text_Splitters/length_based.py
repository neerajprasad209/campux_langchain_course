from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loder = PyPDFLoader("./Document_Loaders/dl-curriculum.pdf")

docs = loder.load()

splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
    separator=''
    
)

result = splitter.split_documents(docs)

print(result[0].page_content)


