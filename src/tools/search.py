from langchain_community.tools.tavily_search import TavilySearchResults

def create_search_tool():
    return TavilySearchResults(max_results=5)
