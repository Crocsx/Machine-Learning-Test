from collections import defaultdict
from gensim import corpora
from gensim import models
from gensim import similarities
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse

parser = argparse.ArgumentParser(description='To Match Sentence')
parser.add_argument('--comments', metavar='S', nargs='?',
                    help='List or comments')
parser.add_argument('--needle', metavar='N', nargs='?',
                    help='Query To Look For Similarity')
args = parser.parse_args()

file = open(args.comments, encoding='utf-8')

documents  = file.readlines()

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [
    [word for word in document.lower().split() if word not in stoplist]
    for document in documents
]
# print(texts)
# remove words that appear only once
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [
    [token for token in text if frequency[token] > 1]
    for text in texts
]

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]


lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

doc = args.needle
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow]  # convert the query to LSI space
# print(vec_lsi)


index = similarities.MatrixSimilarity(lsi[corpus])

sims = index[vec_lsi]  # perform a similarity query against the corpus
# print(list(enumerate(sims)))  # print (document_number, document_similarity) 2-tuples


sims = sorted(enumerate(sims), key=lambda item: -item[1])
for doc_position, doc_score in sims:
    print(doc_score, documents[doc_position])

