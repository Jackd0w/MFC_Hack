from llama_index import ServiceContext, VectorStoreIndex
from data_load import documents

service_context = ServiceContext.from_defaults(chunk_size=512)
index = VectorStoreIndex.from_documents(documents)
print(index)