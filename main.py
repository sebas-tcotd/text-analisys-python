from scraping import obtain_article
from analisys import clean_text, count_words
from visualization import generate_word_cloud, graph_bars


def main():
    url = "http://bbc.com/mundo/articles/c04551g4nk9o"

    text = obtain_article(url)

    if not text:
        print("No se pudo obtener texto alguno del artículo")
        return

    words = clean_text(text)
    counter = count_words(words)

    graph_bars(counter)
    generate_word_cloud(words)


if __name__ == "__main__":
    main()
