from dotenv import load_dotenv
import os
import getpass


load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

model = ChatOpenAI(model_name="gpt-4o-mini")

result = model.invoke([HumanMessage(content="Olá! Me conte uma pequena história.")])

result.pretty_print()