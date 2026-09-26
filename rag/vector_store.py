import chromadb
from rag.documents import load_documents
from rag.embeddings import create_embeddings

def create_vector_store():
    documents=load_documents()
    embeddings=create_embeddings(
        documents
    )
              
    client = chromadb.PersistentClient(
        path="ChromaDB/house_price"
    )
    collection = client.get_or_create_collection(
        name="house_price_knowledge"
    )
    ids = [
        f"doc_{i}"
        for i in range(len(documents))
    ]
    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist()
    )
    return collection          


if __name__ == "__main__":
    collection = create_vector_store()
    print("Vector store created successfully")
    print("Total documents:", collection.count())
                