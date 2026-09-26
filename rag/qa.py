import os
from dotenv import load_dotenv
from openai import OpenAI

from rag.retriever import get_relevant_documents


# Load environment variables
load_dotenv()


# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_answer(question):

    # Retrieve relevant documents
    documents = get_relevant_documents(
        question,
        n_results=2
    )

    # Combine retrieved documents
    context = "\n\n".join(
        documents
    )

    prompt = f"""
You are a helpful AI assistant for a
California House Price Prediction project.

Answer the user's question using the
provided context.

Context:
{context}

Question:
{question}

Give a simple and clear answer.
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":

    question = (
        "What does median income mean "
        "in the California Housing dataset?"
    )

    answer = generate_answer(
        question
    )

    print("\nQuestion:")
    print(question)

    print("\nAI Answer:")
    print(answer)