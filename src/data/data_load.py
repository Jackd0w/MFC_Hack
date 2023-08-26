from llama_index import SimpleDirectoryReader
import logging
import sys
from pathlib import Path
from llama_index import download_loader

PandasExcelReader = download_loader("PandasExcelReader")

loader = PandasExcelReader(pandas_config={"header": 0})
documents = loader.load_data(file=Path('src/data/train_dataset.xlsx'))
print(f'Loaded {len(documents)} docs')
print(type(documents[0]))
'''
db = DatabaseReader(
    scheme="postgresql",  # Database Scheme
    host="localhost",  # Database Host
    port="5432",  # Database Port
    user="postgres",  # Database User
    password="FakeExamplePassword",  # Database Password
    dbname="postgres",  # Database Name
)

print(type(db))
# DatabaseReader available method:
print(type(db.load_data))

### SQLDatabase class ###
# db.sql is an instance of SQLDatabase:
print(type(db.sql_database))
# SQLDatabase available methods:
print(type(db.sql_database.from_uri))
print(type(db.sql_database.get_single_table_info))
print(type(db.sql_database.get_table_columns))
print(type(db.sql_database.get_table_info))
print(type(db.sql_database.get_table_names))
print(type(db.sql_database.insert_into_table))
print(type(db.sql_database.run))
print(type(db.sql_database.run_sql))
# SQLDatabase available properties:
print(type(db.sql_database.dialect))
print(type(db.sql_database.engine))
print(type(db.sql_database.table_info))

query = f"""
    SELECT
        CONCAT(name, ' is ', age, ' years old.') AS text
    FROM public.users
    WHERE age >= 18
    """

documents = db.load_data(query=query)

# Display type(documents) and documents
# type(documents) must return <class 'list'>
print(type(documents))

# Documents must return a list of Document objects
print(documents)


documents = SimpleDirectoryReader('./data').load_data()

index = VectorStoreIndex.from_documents(documents)
'''