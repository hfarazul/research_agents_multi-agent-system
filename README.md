# Multi-Agent Supervisor System

A structured implementation of a multi-agent system with a supervisor that delegates tasks between specialized agents.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your API keys:
```
ANTHROPIC_API_KEY=your-key
TAVILY_API_KEY=your-key
```

3. Run the system:

```bash
python src/main.py
```

## Structure

- `src/agents/`: Contains the different agent implementations
- `src/tools/`: Contains the tools used by agents
- `src/graph/`: Contains the graph structure and state definitions
- `config/`: Contains configuration settings

This structure provides several benefits:
1. Clear separation of concerns
2. Easy to maintain and extend
3. Modular components that can be tested independently
4. Configuration isolated from implementation
5. Clear dependencies between components

To use the system:
1. Create the project structure as shown
2. Copy each file's contents to the appropriate location
3. Install requirements
4. Set up your `.env` file with API keys
5. Run `main.py`

You can easily extend this by:
- Adding new agents in the `agents/` directory
- Adding new tools in the `tools/` directory
- Modifying the graph structure in `graph/builder.py`
- Adding new configuration options in `config/settings.py`
