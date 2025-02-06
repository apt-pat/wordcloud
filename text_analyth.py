from goose3 import Goose
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
#nltk.download('stopwords')

g = Goose()
url = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10599427/'
artigo = g.extract(url)
print(artigo.publish_date)
print(artigo.title)
print(artigo.meta_description)
print(artigo.links)
print(artigo.cleaned_text)


word_tokens = word_tokenize(artigo.cleaned_text)
print(word_tokens)
print(len(word_tokens))


portuguese_stops = set(stopwords.words('portuguese'))

palavras = [palavra for palavra in word_tokens if palavra.lower() not in portuguese_stops]
print(palavras)
print(len(palavras))


fdist = FreqDist(palavras)
#print(fdist.most_common(10))

novas_palavras = [palavra for palavra in palavras if palavra.isalnum()]
fdist= FreqDist(novas_palavras)
print(fdist.most_common(10))


    
mascara = np.array(Image.open("mascara_invertida.png"))
alpha = 0.5 
mascara = (mascara * alpha + 255 * (1 - alpha)).astype(np.uint8)
def plot_cloud(wordcloud):
    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
wordcloud = WordCloud(
    width = 3000,
    height = 2000,
    random_state = 1,
    background_color = 'black',
    colormap = 'Blues',
    collocations = False,
    stopwords = STOPWORDS,
    mask=mascara
).generate(" ".join(novas_palavras))

plot_cloud(wordcloud)