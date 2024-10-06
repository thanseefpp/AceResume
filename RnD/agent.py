from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
import os

_ = load_dotenv()

user_input = "what is the weather in malappuram?"
memory = MemorySaver()
search = TavilySearchResults(
        max_results=3,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=True,
        include_images=True
    )
model = ChatOpenAI(model="gpt-4o-mini",api_key=os.environ["OPENAI_API_KEY"])
search_results = search.invoke(user_input)
tools = [search]
config = {"configurable": {"thread_id": "abc123"}}
agent_executor = create_react_agent(model, tools, checkpointer=memory)
response = agent_executor.invoke(
    {"messages": [HumanMessage(content=user_input)]},config
)

print(f"response : {response['messages']}")
print(response)