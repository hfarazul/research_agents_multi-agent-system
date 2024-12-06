from langgraph.graph import StateGraph, START, END
from src.graph.state import AgentState
from src.agents.supervisor import create_supervisor
from src.agents.researcher import create_researcher
from src.agents.coder import create_coder

def build_graph():
    """Build the agent interaction graph."""
    # Create nodes
    supervisor = create_supervisor()
    research_node = create_researcher()
    code_node = create_coder()

    # Initialize graph
    builder = StateGraph(AgentState)

    # Add nodes
    builder.add_node("supervisor", supervisor)
    builder.add_node("researcher", research_node)
    builder.add_node("coder", code_node)

    # Add edges
    members = ["researcher", "coder"]
    for member in members:
        builder.add_edge(member, "supervisor")

    # Add conditional routing
    builder.add_conditional_edges(
        "supervisor",
        lambda state: state["next"] if state["next"] != "FINISH" else END
    )

    # Add entry point
    builder.add_edge(START, "supervisor")

    return builder.compile()
