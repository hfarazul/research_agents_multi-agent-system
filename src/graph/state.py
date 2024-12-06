from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import MessagesState

class AgentState(MessagesState):
    """The agent state with routing information."""
    next: str

class Router(TypedDict):
    """Type definition for routing between agents."""
    next: Literal["researcher", "coder", "FINISH"]
