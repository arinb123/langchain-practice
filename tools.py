from langchain.tools import tool

@tool
def reverse_text(text: str) -> str:
    """Reverses a string."""
    return text[::-1]
