"""
Runs the base LangGraph agent from src/base_agent.py.
You can later import and expand this with new tools or custom nodes.
"""
from src.base_agent import graph

print("Running base LangGraph agent...\n")
result = graph.invoke({"messages": [{"role": "user", "content": "hello!"}]})
print("AI:", result["messages"][-1]["content"])
