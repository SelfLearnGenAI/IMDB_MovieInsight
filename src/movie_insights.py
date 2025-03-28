import os
import chromadb
from chromadb.utils import embedding_functions
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from src.constants import *
from src.utils import get_vector_store_documents, load_data_into_chroma

chroma_client = chromadb.Client()
openai_ef = embedding_functions.OpenAIEmbeddingFunction(api_key=OPENAI_API_KEY, model_name=EMBEDDING_MODEL_NAME)
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
llm = ChatOpenAI(model=LLM_MODEL_NAME)

collection = load_data_into_chroma(openai_ef, chroma_client)

system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of context to answer the question. If you don't know the answer, say that you don't "
    "know. Use three sentences maximum and keep the answer concise."
    "The context is strictly in json format with fields such as title, year of release, genre, imdb rating and brief "
    "introduction\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)


llm_chain = prompt | llm

query = "movies directed by christopher nolan"
vector_store_documents = get_vector_store_documents(collection, openai_ef, query)

response = llm_chain.invoke({"input": query, "context": "\n\n".join(vector_store_documents)})
print(response.content)
