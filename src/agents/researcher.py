from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from src.tools.search import create_search_tool
from src.graph.state import AgentState
from config.settings import LLM_MODEL

def create_researcher():
    """Create the researcher agent for web searches."""
    llm = ChatOpenAI(model=LLM_MODEL)
    search_tool = create_search_tool()

    research_agent = create_react_agent(
        llm,
        tools=[search_tool],
        state_modifier="You are a researcher. DO NOT do any math."
    )

    def research_node(state: AgentState):
        result = research_agent.invoke(state)
        return {
            "messages": [
                HumanMessage(
                    content=result["messages"][-1].content,
                    name="researcher"
                )
            ]
        }

    return research_node
