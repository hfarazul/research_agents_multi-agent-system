from src.graph.builder import build_graph

def run_team(query: str):
    """Execute the multi-agent system on a query."""
    graph = build_graph()

    for step in graph.stream(
        {"messages": [("user", query)]},
        subgraphs=True
    ):
        print(step)
        print("----")

if __name__ == "__main__":
    query = input("Enter your query: ")
    run_team(query)
