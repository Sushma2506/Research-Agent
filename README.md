# 🔍 Research Agent

An AI-powered research assistant built with [Ollama](https://ollama.com/) and the Llama 3.2 model. It uses tool-calling to perform web searches and save structured reports to files — all through an interactive command-line interface.

## Features

- **Web Search** — Query the web for information on any topic
- **Report Generation** — Automatically save research findings to a file with key highlights
- **Interactive Chat** — Conversational loop so you can refine queries and ask follow-ups
- **Tool Calling** — Uses Ollama's native tool-calling API for structured, reliable function execution

## Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/download) installed and running locally
- The **Llama 3.2** model pulled:
  ```bash
  ollama pull llama3.2
  ```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sushma2506/Research-Agent.git
   cd Research-Agent
   ```

2. **Install the Python dependency:**
   ```bash
   pip install ollama
   ```

## Usage

Run the agent:

```bash
python Agent-1.py
```

You'll be greeted with an interactive prompt. Ask it to research any topic or save a report:

```
Hi, How may I help you?
> Research the latest trends in AI and save a report
```

Type `quit` or `exit` to end the session.

## Project Structure

```
Research-Agent/
├── Agent-1.py     # Main agent script with tool definitions and chat loop
└── README.md
```

## How It Works

1. The user enters a query via the CLI.
2. The agent sends the query to the Llama 3.2 model along with available tool definitions.
3. The model decides which tool(s) to call:
   - `web_search` — Searches the web for the given query.
   - `save_report` — Saves the generated report (with key findings) to a local file.
4. Tool results are fed back into the conversation for the model to produce a final response.
5. The loop continues until the user types `quit` or `exit`.

## License

This project is open source and available under the [MIT License](LICENSE).
