from llama_index.node_parser import SimpleNodeParser
from data_load import documents

# Cоздаем парсер
parser = SimpleNodeParser()

# Разбиваем на ноды
nodes = parser.get_nodes_from_documents(documents)

print(type(nodes))

    
