import re
from collections import Counter


def clean_text(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r"[^a-záéíóúñ\s]", "", text)
    words = text.split()

    stopwords = {
        "de",
        "la",
        "que",
        "el",
        "en",
        "los",
        "las",
        "por",
        "del",
        "se",
        "con",
        "una",
        "como",
        "más",
        "para",
        "sus",
        "entre",
        "pero",
    }
    words = [word for word in words if word not in stopwords and len(word) > 3]

    return words


def count_words(words: list[str]) -> list[tuple[str, int]]:
    return Counter(words).most_common(20)
