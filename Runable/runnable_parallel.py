from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser


from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a Blog about {topic}. ",
    input_variables=['topic'],
)

prompt2 = PromptTemplate(
    template="Write a linkedin post about: {topic}. ",
    input_variables=['topic'],
)

model = ChatOpenAI(model='gpt-4o')

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "blog": RunnableSequence(prompt1, model, parser),
    "linkedin": RunnableSequence(prompt2, model, parser),
})

result = parallel_chain.invoke({"topic": "AI in Healthcare"})

print("Blog\n",result['blog'])
print("\n======================================================\n")
print("Linkedin\n",result['linkedin'])