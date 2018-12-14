import pandas as pd
import numpy as np
from gensim.models.keyedvectors import KeyedVectors
import gensim.downloader as api


def get_corpus(corpus_):
    """Loads pre-trained word2vec model from src/ directory and 
    returns a gensim word2vec object"""
    if corpus_ == 'google':
        return api.load('word2vec-google-news-300')

    if corpus_=='glove':
        return api.load('glove-twitter-50')

    if corpus_=='fasttext':
        return api.load('fasttext-wiki-news-subwords-300')


if __name__ == '__main__':
    model = get_corpus('glove')
