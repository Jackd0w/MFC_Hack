import pandas as pd
df = pd.read_excel('src/data/train_dataset.xlsx') # can also index sheet by name or fetch all sheets

question_list = df['QUESTION'].tolist()
answer_list = df['ANSWER'].tolist()
