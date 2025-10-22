# LangGraph Agent Development Tasks

Your goal: **extend the base LangGraph example** into a more advanced AI agent that can perform simple research or data-processing tasks using tools and reasoning steps.

---

## Task Overview

1. **Understand the base agent**

   * Read through `src/base_agent.py`
   * Identify how the agent:

     * Uses `StateGraph`
     * Defines a node (the `chat_node`)
     * Connects nodes using edges
     * Invokes the graph with messages

2. **Create your own agent**

   * Copy `src/my_agent_template.py`
   * Build an agent that includes at least **two nodes**:

     1. A **tool node** that performs a simple function (e.g., reversing text, searching, math, or calling an API)
     2. An **LLM node** that summarizes or explains the tool’s output

   Example flow:

   ```
   START → tool_node → llm_node → END
   ```

3. **Use tools**

   * Tools are functions you import from `tools.py` or define yourself.
   * Example:

     ```python
     from tools import reverse_text
     ```
   * You can wrap your tool logic in a LangGraph node:

     ```python
     def tool_node(state):
         text = state["messages"][-1]["content"]
         result = reverse_text(text)
         return {"messages": [{"role": "tool", "content": result}]}
     ```

4. **Make it interactive**

   * Just like `base_agent.py`, allow user input from the command line.
   * Each time a user enters text, send it into your agent graph and print the output.

5. **Bonus challenges (optional)**

   * Add memory between runs (so the agent “remembers” past messages)
   * Add a decision node that routes between multiple tools
   * Log agent reasoning steps or visualize graph execution

---

## Deliverable

By the end, you should have:

* A **working script** in `src/my_agent_template.py`
* At least **two connected nodes**
* Evidence that it runs correctly (screenshots or logs)

---

## Resources

* LangGraph Docs: [https://docs.langchain.com/oss/python/langchain/overview?_gl=1*16ti1yo*_ga*MTYxMDY5NDM1MS4xNzYxMDkzMTYx*_ga_47WX3HKKY2*czE3NjEwOTMxNjEkbzEkZzEkdDE3NjEwOTQ3MDkkajYwJGwwJGgw](https://docs.langchain.com/oss/python/langchain/overview?_gl=1*16ti1yo*_ga*MTYxMDY5NDM1MS4xNzYxMDkzMTYx*_ga_47WX3HKKY2*czE3NjEwOTMxNjEkbzEkZzEkdDE3NjEwOTQ3MDkkajYwJGwwJGgw)
* LangChain Docs: [https://docs.langchain.com/oss/python/langgraph/overview](https://docs.langchain.com/oss/python/langgraph/overview)
* Example from base agent:

  ```python
  graph.invoke({"messages": [{"role": "user", "content": "hello"}]})
  ```

---

 **Goal:** Think like an agent designer — how should your system pass state, call tools, and respond intelligently?
