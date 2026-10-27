from ollama import chat

MODEL_NAME = "qwen3:1.7b"


def generate_response(prompt: str) -> str:
    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        think=False,
        options={
            "temperature": 0
        }
    )

    return response.message.content or ""