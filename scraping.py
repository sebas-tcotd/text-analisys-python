import requests
from bs4 import BeautifulSoup


def obtain_article(url: str) -> str:
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error al acceder a la URL: {response.status_code}")
            return ""

        soup = BeautifulSoup(response.text, "html.parser")
        parrafos = soup.find_all("p")

        if not parrafos:
            print("No se encontraron párrafos en la página.")
            return ""

        texto = " ".join([p.get_text() for p in parrafos])
        return texto

    except Exception as e:
        print(f"Error al obtener artículo: {e}")
        return ""
