from ollama import chat


class Generator:

    def __init__(self, model_name="qwen2.5:3b"):
        self.model_name = model_name

    def generate(self, question, context):
        prompt = f"""
You are a document question-answering assistant.

Answer the question using only the provided context.

If the answer cannot be found in the context, say:
"I don't have enough information in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

        response = chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]