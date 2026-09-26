from sentence_transformers import SentenceTransformer
from rag.documents import load_documents
def create_embeddings(documents):
    model=SentenceTransformer(
        "all-MiniLM-L6-v2"
    )
    embeddings=model.encode(
        documents
    )
    return embeddings

if __name__=="__main__":
    documents = load_documents()
    embeddings =create_embeddings(
        documents
    )
    
    print("Embedding created successfully")
    print("Number of embedding:", len(embeddings))
    print("Embedding :",len(embeddings[0]))
