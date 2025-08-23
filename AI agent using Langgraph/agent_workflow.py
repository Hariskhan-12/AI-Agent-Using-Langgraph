from langgraph.graph import StateGraph, END
from langchain.agents import Tool
from tools.search_tool import search_web
from tools.calc_tool import calculate
from llm.llm import get_llm

def create_agent():
    llm = get_llm()

    # Define tools
    tools = [
        Tool(name="WebSearch", func=search_web, description="Perform web search"),
        Tool(name="Calculator", func=calculate, description="Perform calculations")
    ]

    # Build agent graph
    workflow = StateGraph()
    workflow.add_node("start", lambda state: {"query": state["query"]})
    workflow.add_node("llm", lambda state: {"answer": llm.predict(state["query"])})
    workflow.add_edge("start", "llm")
    workflow.add_edge("llm", END)

    workflow.set_entry_point("start")
    return workflow.compile()
