# Usamos una imagen base de Python 3.11.4
FROM python:3.11.4-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos los archivos de requerimientos al contenedor
COPY requirements.txt .

# Instalamos `pip` y `setuptools` actualizados
RUN pip install --upgrade pip setuptools \
    && pip install -r requirements.txt

# Instalamos las dependencias del sistema necesarias para SpaCy y modelos
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libbz2-dev \
    liblzma-dev \
    libsqlite3-dev \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libreadline-dev \
    libssl-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Instalamos SpaCy, `sentence-transformers`, `nltk`, y `werkzeug`
RUN pip install spacy sentence-transformers nltk werkzeug

# Instalamos una versión específica de NumPy
RUN pip install numpy==1.24.4

# Descargamos el modelo de SpaCy
RUN python -m spacy download es_core_news_sm

# Copiamos el resto de los archivos del proyecto al contenedor
COPY . .

# Copiamos el archivo de variables de entorno
COPY .env .env

# Exponemos el puerto en el que la aplicación correrá
EXPOSE 3000

# Definimos el comando para iniciar la aplicación
CMD ["python", "app.py"]
