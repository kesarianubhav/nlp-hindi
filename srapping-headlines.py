# from urllib.request import urlopen
# from bs4 import BeautifulSoup
import multiprocessing
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from gensim.models.word2vec import Word2Vec
url = "https://m.dailyhunt.in/news/india/hindi/bbc+hindi-epaper-bbchind/vijay+malya+ka+dava+desh+chodane+se+pahale+vitt+mantri+arun+jetali+se+mila+tha-newsid-96783198"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(url, headers=hdr)
web_page = urlopen(req)

soup = BeautifulSoup(web_page, 'html.parser')

headline = soup.findAll("p", {"style": ""})
# print(headline)

for i in headline:

    # for i in headline:
    #     words = (i.text).strip().split()
    #     for j in words:
    #         print(j)
    sentence = i.text
    params = {'size': 200, 'window': 10, 'min_count': 1,
              'workers': max(1, multiprocessing.cpu_count() - 1), 'sample': 1E-3, }
    word2vec = Word2Vec(sentence, **params)
    for i in word2vec:
        print(i)
