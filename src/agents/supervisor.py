from langchain_openai import ChatOpenAI
from src.graph.state import AgentState, Router
from config.settings import LLM_MODEL

def create_supervisor():
    """Create the supervisor agent that delegates tasks."""
    members = ["researcher", "coder"]
    system_prompt = (
        "You are a supervisor managing conversations between these workers: "
        f"{members}. Given the user request, respond with the next worker "
        "to act. When finished, respond with FINISH."
    )

    llm = ChatOpenAI(model=LLM_MODEL)

    def supervisor_node(state: AgentState):
        messages = [
            {"role": "system", "content": system_prompt},
        ] + state["messages"]
        response = llm.with_structured_output(Router).invoke(messages)
        return {"next": response["next"]}

    return supervisor_node
