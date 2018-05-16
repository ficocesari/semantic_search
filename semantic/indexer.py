import logging
import os
import tempfile
from gensim import corpora
from gensim.parsing.preprocessing import STOPWORDS
from pprint import pprint  # pretty-printer
from collections import defaultdict


class Indexer:

    def __init__(self):
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        self.TEMP_FOLDER = tempfile.gettempdir()
        print('Folder "{}" will be used to save temporary dictionary and corpus.'.format(self.TEMP_FOLDER))

        self.documents = None

    def set_documents(self, documents):
        if documents is None:
            self.documents = ["Human machine interface for lab abc computer applications",
                              "A survey of user opinion of computer system response time",
                              "The EPS user interface management system",
                              "System and human system engineering testing of EPS",
                              "Relation of user perceived response time to error measurement",
                              "The generation of random binary unordered trees",
                              "The intersection graph of paths in trees",
                              "Graph minors IV Widths of trees and well quasi ordering",
                              "Graph minors A survey"]
        else:
            self.documents = documents

    def remove_stopwords(self):
        # remove common words and tokenize
        texts = [[word for word in document.lower().split() if word not in STOPWORDS]
                 for document in self.documents]
        return texts

    def clean_low_freq_words(self, texts):
        # remove words that appear only once
        frequency = defaultdict(int)
        for text in texts:
            for token in text:
                frequency[token] += 1

        texts = [[token for token in text if frequency[token] > 1] for text in texts]

        pprint(texts)


if __name__ == "__main__":
    indexer = Indexer()
    indexer.set_documents(None)
    texts = indexer.remove_stopwords()
    indexer.clean_low_freq_words(texts)
