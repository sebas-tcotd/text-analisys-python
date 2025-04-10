# 🧠 Tendencias de Texto Web con Python

Este proyecto explora el análisis automatizado de artículos web en español mediante técnicas de scraping, procesamiento de lenguaje natural (NLP) y visualización de datos.

---

## 🔍 ¿Qué hace?

1. Obtiene texto desde un artículo web usando `requests` + `BeautifulSoup`
2. Limpia el texto y extrae palabras significativas
3. Cuenta las palabras más frecuentes
4. Visualiza los resultados con gráficos y nube de palabras (`matplotlib` + `wordcloud`)
5. Todo documentado y ejecutable desde Jupyter Notebook

---

## 📦 Tecnologías usadas

- `Python 3`
- `Jupyter Notebook`
- `requests`
- `BeautifulSoup4`
- `matplotlib`
- `wordcloud`

> Proximamente: `spaCy` para lematización y detección de entidades (NER)

---

## 📁 Estructura del repositorio

```bash
.
├── scraping.py          # Obtiene texto desde una URL
├── analisis.py          # Limpia texto y analiza palabras
├── visualizacion.py     # Gráficos y nube de palabras
├── main.py              # Script principal (orquestra todo)
├── tendencias-texto.ipynb  # Cuaderno interactivo con el flujo completo
├── datos/               # donde se guarda texto (maybe in the future)
├── requirements.txt     # Dependencias mínimas del proyecto
└── README.md
```

## ⚙️ ¿Cómo ejecutarlo?

```bash
git clone https://github.com/tu-usuario/tendencias-texto.git
cd tendencias-texto

# Crear y activar entorno virtual (opcional)
python -m venv env
source env/bin/activate  # o .\env\Scripts\activate en Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar script completo (modo terminal)
python main.py

# O lanzar el notebook interactivo
jupyter notebook
```

## 💡 Ideas de expansión

- Scraping múltiple (varios artículos)
- Lematización de palabras
- Detección de entidades (NER)
- Clasificación por temas o clustering de artículos
- Publicación como app web con Streamlit o FastAPI

## 🤖 Autor

Sebastian Vargas P.

Ingeniero de software | Artista polifacético | Explorador de ideas
[LinkedIn](https://www.linkedin.com/in/sebas-vargas/) – [GitHub](https://github.com/sebas-tcotd)
