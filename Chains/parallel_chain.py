from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

from dotenv import load_dotenv

load_dotenv()


model_openai = ChatOpenAI(model='gpt-4o')
model_genai = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

prompt_1 = PromptTemplate(
    template="Generate short and simple from the following text:\n{text}. ",
    input_variables=['text'],
)

prompt_2 = PromptTemplate(
    template="Generate 5 short Question and Answer from the following text:\n{text}. ",
    input_variables=['text'],)

final_prompt = PromptTemplate(
    template = "Merge the provided notes and the quiz into the single document:\n notes: {notes}\n quiz: {quiz}. ",
    input_variables=['input_1', 'input_2'],)

parser = StrOutputParser()


parallel_chain = RunnableParallel({
    "notes": prompt_1 | model_openai | parser,
    "quiz": prompt_2 | model_genai | parser
})

merged_chain =  final_prompt | model_openai | parser

chain = parallel_chain | merged_chain

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

result = chain.invoke({"text": text})

print(result)

chain.get_graph().print_ascii()

