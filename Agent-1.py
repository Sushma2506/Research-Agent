import ollama


tools = [
    # tool 1
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Do research for the query",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search term to look up",
                    },
                },
                "required": ["query"],
            },
        },
    },
    # tool 2
    {
        "type": "function",
        "function": {
            "name": "save_report",
            "description": "Save the report to a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_name": {
                        "type": "string",
                        "description": "The name of the file to save the report to",
                    },
                    "key_findings": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "The key findings of the report",
                    },
                    "content": {"type": "string", "description": "final output"},
                },
            },
            "required": ["file_name", "key_findings", "content"],
        },
    },
]


def web_search(query):
    return f"Here are some results for {query}: ..."


def save_report(file_name, key_findings, content):
    print(f"save_report called with file_name: {file_name}")
    with open(file_name, "w") as file:
        file.write(content)
    return f"Report saved to {file_name}"


def get_arg(arg):
    if isinstance(arg, dict):
        return arg.get("value", arg)
    return arg


if __name__ == "__main__":
    query = input(f"Hi, How may I help you?" + "\n")
    model = "llama3.2"
    options = {"temperature": 0}
    messages = [
        {
            "role": "system",
            "content": """You are a research assistant with two tools:
                        1. web_search - use this to search for information
                        2. save_report - use this WHENEVER the user asks to save, write, or store anything to a file

                        When user asks to save content to a file, you MUST call save_report tool. Never just respond with text when saving is requested.""",
        },
        {"role": "user", "content": query},
    ]
    while True:
        response = ollama.chat(model=model, messages=messages, tools=tools)
        if response.message.tool_calls:
            for tool in response.message.tool_calls:
                print(f"Tool called: {tool.function.name}")
                if tool.function.name == "web_search":
                    result = web_search(get_arg(tool.function.arguments["query"]))
                    print(tool.function.arguments)
                    messages.append({"role": "tool", "content": result})
                elif tool.function.name == "save_report":
                    result = save_report(
                        get_arg(
                            tool.function.arguments["file_name"],
                            tool.function.arguments["key_findings"],
                            tool.function.arguments["content"],
                        )
                    )
                    messages.append({"role": "tool", "content": result})
            response = ollama.chat(model=model, messages=messages)
            print(response.message.content)
            query = input(f"Reply.." + "\n")
            messages.append({"role": "tool", "content": query})
        else:
            print(response.message.content)
            query = input("Reply (or 'quit' to exit): ")
            if query.lower() in ["quit", "exit"]:
                break
            messages.append({"role": "user", "content": query})
