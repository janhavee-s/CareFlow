from langchain_ollama import ChatOllama


def get_llm():
    return ChatOllama(
        model="mistral",     # or "mistral"
        temperature=0.2,
    )


llm = get_llm()
