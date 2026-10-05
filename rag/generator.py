from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def generate_answer(question, documents):
    context = "\n\n".join(documents)

    prompt = f"""
You are an AI assistant for a House Price Prediction project.
Answer the user's question using only the provided context.

Context:
{context}

Question:
{question}

Give a simple and clear answer.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text