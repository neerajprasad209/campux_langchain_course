from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o')

parser = StrOutputParser()

class feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt_1 = PromptTemplate(
    template="Classify the Sentiment of the following text into positive or negative \n {feedback}. \n {format_instructions}",
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser2.get_format_instructions()},
    
)


classifier_chain = prompt_1 | model | parser2

prompt_2 = PromptTemplate(
    template="Write a appropriate response to this positive feedback\n {feedback}. ",
    input_variables=['feedback'],
)

prompt_3 = PromptTemplate(
    template="Write a appropriate response to this nagative feedback\n {feedback}. ",
    input_variables=['feedback'],
)


branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt_2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt_3 | model | parser),
    RunnableLambda(lambda x: "Could not classify sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()