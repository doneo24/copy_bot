from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex

def build_index():
    documents = SimpleDirectoryReader('./data').load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    index.save_to_disk('index.json')

if __name__ == '__main__':
    build_index()