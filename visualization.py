import matplotlib.pyplot as plt
from wordcloud import WordCloud


def graph_bars(counter: list[tuple[str, int]]):
    words, frecs = zip(*counter)
    plt.figure(figsize=(10, 5))
    plt.bar(words, frecs)
    plt.xticks(rotation=45)
    plt.title("Palabras más frecuentes")
    plt.tight_layout()
    plt.show()


def generate_word_cloud(words: list[str]):
    text = " ".join(words)
    cloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Nube de palabras")
    plt.show()
