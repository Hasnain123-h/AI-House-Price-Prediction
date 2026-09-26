import chromadb

from sentence_transformers import SentenceTransformer


# Load embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def get_relevant_documents(
    question,
    n_results=2
):
    """
    Find the most relevant documents
    from ChromaDB for the given question.
    """

    # Connect to ChromaDB
    client = chromadb.PersistentClient(
        path="ChromaDB/house_price"
    )

    # Get existing collection
    collection = client.get_collection(
        name="house_price_knowledge"
    )

    # Convert question into embedding
    query_embedding = embedding_model.encode(
        question
    )

    # Search similar documents
    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=n_results
    )

    # Extract documents
    documents = results["documents"][0]

    return documents


if __name__ == "__main__":

    question = (
        "What does median income mean "
        "in the California Housing dataset?"
    )

    documents = get_relevant_documents(
        question
    )

    print("Question:")
    print(question)

    print("\nRelevant Documents:")

    for i, document in enumerate(
        documents,
        start=1
    ):
        print(f"\nDocument {i}:")
        print(document)
     