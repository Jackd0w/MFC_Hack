from llama_index import VectorStoreIndex, Document, ServiceContext
from llama_index.llms import HuggingFaceLLM
import torch
from embedding import sentence_embeddings



llm = HuggingFaceLLM(
    context_window=2048,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.25, "do_sample": False},
    tokenizer_name="ai-forever/sbert_large_mt_nlu_ru",
    model_name="ai-forever/sbert_large_mt_nlu_ru",
    device_map="cpu",
    tokenizer_kwargs={"max_length": 2048},
    # uncomment this if using CUDA to reduce memory usage
    # model_kwargs={"torch_dtype": torch.float16}
)
service_context = ServiceContext.from_defaults(chunk_size=512, llm=llm)

#index = VectorStoreIndex.from_documents(documents, service_context=service_context)

query_engine = sentence_embeddings.as_query_engine(streaming=True)

response_stream = query_engine.query("При каких условиях назначается и выплачивается пособие?")

response_stream.print_response_stream()