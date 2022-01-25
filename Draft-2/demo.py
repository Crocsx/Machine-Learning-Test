import gensim.downloader as api
wv = api.load('word2vec-google-news-300')


print(wv.most_similar(positive=['car', 'minivan'], topn=5))