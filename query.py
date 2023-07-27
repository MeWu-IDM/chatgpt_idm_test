import pickle

import faiss
from langchain import OpenAI
# from langchain.chains import VectorDBQAWithSourcesChain (deprecated
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
import argparse

def ask_db(store, question, temperature=0.5):
    chain = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=temperature, model_name="gpt-3.5-turbo"),
        chain_type="stuff",
        retriever=store.as_retriever(),
        return_source_documents=True
    )
    result = chain({"query": question})
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='www.idmod.org Q&A')
    parser.add_argument('question', type=str, help='Your question for idmod')
    args = parser.parse_args()

    with open("faiss_store.pkl", "rb") as f:
        store = pickle.load(f)

    # chain = VectorDBQAWithSourcesChain.from_llm(
    #             llm=OpenAI(temperature=0.5), vectorstore=store)
    # llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, max_tokens=256)
    result = ask_db(store, args.question)
    print(f"Answer: {result['result']}")
    print(f"Sources: {result['source_documents']}")

