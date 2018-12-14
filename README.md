# NLP data augmentation

This repository started as code snippets that were created as part of [Konstantin Hemker's](https://github.com/KonstantinHemker/NLP-data-augmentation) Master's Thesis on NLP at Imperial College London. Currently there are two similar techniques, based on replacing words nearby in word2vec space.

This fork plans on adding many more techniques.

## Installation

### Python requirements

##### Python version: 3

Only tested on 3.6.

##### Dependencies

Uses [Pipenv](https://pipenv.readthedocs.io/en/latest/). Install deps with `pipenv install`. Run commands like `pipenv run python augment.py`, or launch a shell in the automatically created venv with `pipenv shell`.

### Other dependencies

~Most models require pre-trained word vector models. As these models are relatively large, I ommitted them from the git repo. To download the files automatically, run the shell script ```./pretrained_vectors.sh```~

Models are downloaded as needed using `gensim.downloader`, which is automatically called by Gensim. See more [here](https://github.com/RaRe-Technologies/gensim-data). Currently the models it downloads are hardcoded, but this should probably be configurable.

## Methods
### Threshold
Loads in a word embedding pre-trained on one of the large text corpora given above. Replaces the words in a sentence with their highest cosine similarity word vector neighbour that exceed a threshold given as an argument.

### POS-tag
Replaces all words of a given POS-tag (given as argument) in the sentence with their most similar word vector from a large pre-trained word embedding.

### Generative
The idea of this is: train a two-layer LSTM network to learn the word representations of given class. The network then generates new samples of the class by initialising a random start word and following the LSTM's predictions of the next word given the previous sequence. 

However, this hasn't been implemented yet.


## Input
Takes in a CSV file with mutually exclusive, numerical labels and text input. The arguments for the Augment object are as follows:

```Augment(method, source_path, target_path, corpus_='none',```
```valid_tags=['NN'], threshold=0.75, x_col='tweet', y_col='class')```

- `method`: Which of the three augmentation methods should be used
  (valid args: 'threshold', 'postag', 'generate')
- `source_path`: Path of the input csv file (type: string)
- `target_path`: Path of the output csv file (type: string)
- `corpus`: Text corpus of pre-trained word embeddings that should
  be used (valid args: 'google', 'glove', 'fasttext')
- `valid_tags`: POS-tags of words that should be replaced in the
  POS-tag based method (type: list of strings)
- `threshold`: Threshold hyperparameter when threshold-based
  augmentation is used (type: float)
- `x_col`: Column name of the samples in input CSV file (type: string)
- `y_col`: Column name of the labels in input CSV file (type: string)

## Fork Plan

### DX improvements

* Make this work in python 2 or 3
* Minimize downloads (use local glove if available)
* Put on pip / conda
* Make sure integration with pandas, scikit-learn is easy and well-documented
* Possibly make this a plugin to fastai?

### Functionality improvements

* Add new augmentation techniques:
    - [Roundtrip translation](https://github.com/samhavens/roundtrip), as mentioned in [QANET: COMBINING LOCAL CONVOLUTION WITH GLOBAL SELF-ATTENTION FOR READING COMPREHENSION](https://openreview.net/pdf?id=B14TlG-RW)
    - [Contextual Augmentation](https://github.com/pfnet-research/contextual_augmentation), based on the paper [Contextual Augmentation: Data Augmentation by Words with Paradigmatic Relations](https://arxiv.org/abs/1805.06201)
    - N-gram replacement and blanking (need to write this, I think), from [DATA NOISING AS SMOOTHING IN NEURAL NETWORK
LANGUAGE MODELS](https://arxiv.org/pdf/1703.02573.pdf)

