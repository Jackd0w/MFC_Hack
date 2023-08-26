from llama_index import ListIndex, SimpleDirectoryReader, ServiceContext
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index import LangchainEmbedding
from node__parser import nodes
from typing import List
from langchain.embeddings.base import Embeddings
from sentence_transformers import SentenceTransformer

model_name = "ai-forever/sbert_large_nlu_ru"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)



index = hf.embed_documents(nodes)
print(index)

def embed_documents(self, texts: List[str]) -> List[List[float]]:
    embeddings = hf.encode(texts)
    return embeddings

def embed_query(self, text: str) -> List[float]:

        embedding = self.model.encode(text)
        return list(map(float, embedding))

