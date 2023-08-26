import pandas as pd
from transformers import pipeline
from transformers.pipelines.pt_utils import KeyDataset
from tqdm.auto import tqdm

oracle = pipeline(
    model="timpal0l/mdeberta-v3-base-squad2", tokenizer="ai-forever/sbert_large_nlu_ru"
)

pipe = pipeline("question-answering", model="timpal0l/mdeberta-v3-base-squad2")
print(pipe(
    image="src/data/train_dataset.xlsx",
    question="Какие основания для детской карты?"
))

