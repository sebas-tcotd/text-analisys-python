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

---

## 🔬 Análisis avanzado con spaCy

En esta nueva etapa del proyecto, se integró [spaCy](https://spacy.io/) para aplicar técnicas más sofisticadas de procesamiento de lenguaje natural:

- ✅ **Lematización**: reduce palabras a su forma base (por ejemplo, "estudiando" → "estudiar")
- ✅ **NER (Named Entity Recognition)**: identifica entidades como personas, lugares, fechas, organizaciones, etc.

### 🧠 Ejemplo de uso con spaCy

```python
import spacy
nlp = spacy.load("es_core_news_sm")
doc = nlp("Pedro Castillo fue elegido presidente del Perú en 2021.")

for ent in doc.ents:
    print(ent.text, ent.label_)
```

### ⚠️ Compatibilidad de versiones

Nota: spaCy actualmente no es compatible con Python 3.13.
Se recomienda usar Python 3.10 o 3.11. Puedes mantener múltiples versiones usando entornos virtuales personalizados sin necesidad de hacer downgrade global.

### ✅ Instalación del modelo de español localmente

```bash
pip install https://github.com/explosion/spacy-models/releases/download/es_core_news_sm-3.7.0/es_core_news_sm-3.7.0-py3-none-any.whl
```

Una vez instalado el modelo, el análisis avanzado está listo para ejecutarse dentro del mismo Jupyter Notebook.

---

### 🧠 Detección de entidades nombradas (NER)

Con `spaCy`, también se pueden detectar automáticamente entidades como personas, países, fechas, organizaciones, entre otros.

#### 🧪 Ejemplo de código

```python
for ent in doc.ents:
    print(ent.text, ent.label_)
```

##### 📋 Ejemplo de salida

```sql
Pedro Castillo → PER
Perú → LOC
2021 → DATE
```

| Etiqueta  | Significado               |
| --        | --                        |
| `PER`     | Persona                   |
| `LOC`     | Lugar (localización)      |
| `ORG`     | Organización              |
| `DATE`    | Fecha                     |
| `MONEY`   | Monto monetario           |
| `GPE`     | País o entidad política   |

Esta funcionalidad puede ser muy útil para:

- Extraer nombres y ubicaciones mencionadas en noticias
- Hacer dashboards temáticos
- Detectar menciones clave en textos grandes

_Nota_: Los resultados pueden variar dependiendo de la redacción del artículo, pero aún así representan una herramienta poderosa para análisis semánticos.

## 💡 Ideas de expansión

- Scraping múltiple (varios artículos)
- Clasificación por temas o clustering de artículos
- Publicación como app web con Streamlit o FastAPI

## 🤖 Autor

Sebastian Vargas P.

Ingeniero de software | Artista polifacético | Explorador de ideas

[LinkedIn](https://www.linkedin.com/in/sebas-vargas/) – [GitHub](https://github.com/sebas-tcotd)
