from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from src.tools.code_executor import python_repl_tool
from src.graph.state import AgentState
from config.settings import LLM_MODEL

def create_coder():
    """Create the coder agent for executing Python code."""
    llm = ChatOpenAI(model=LLM_MODEL)

    code_agent = create_react_agent(
        llm,
        tools=[python_repl_tool]
    )

    def code_node(state: AgentState):
        result = code_agent.invoke(state)
        return {
            "messages": [
                HumanMessage(
                    content=result["messages"][-1].content,
                    name="coder"
                )
            ]
        }

    return code_node
