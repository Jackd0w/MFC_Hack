from llama_index.node_parser import SimpleNodeParser
from data_load import documents

parser = SimpleNodeParser.from_defaults()

nodes = parser.get_nodes_from_documents(documents)
