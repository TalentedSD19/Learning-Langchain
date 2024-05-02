from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes  # type: ignore
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(title="Langchain Server", version="1.0", description="api server")

add_routes(app, ChatOpenAI(), path="/openai")

model1 = ChatOpenAI(model="gpt-3.5-turbo")
model2 = Ollama(model="llama3")

prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words."
)
prompt2 = ChatPromptTemplate.from_template(
    "Write me an poem about {topic} with 100 words."
)

add_routes(app, prompt1 | model1, path="/essay")

add_routes(app, prompt2 | model2, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
