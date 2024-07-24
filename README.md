# FIS Chatbot API

A **rules-based chatbot** API that answers frequently asked questions from FIS students.

## Content
[1. Description](#1-description)  
[2. Requirements](#2-requirements)  
&nbsp;&nbsp;&nbsp;&nbsp;[2.1. Dependencies](#21-dependencies)  
&nbsp;&nbsp;&nbsp;&nbsp;[2.2. Environment Variables](#22-environment-variables)

## 1. Description

The API is responsible for receiving messages to generate various types of responses, such as text, images, links, 
actions and forms. The API currently uses calculations supported by **Cosine Similarity** to identify user intent.
Then, the intent is associated with a given response and is sent to the user.

## 2. Requirements

### 2.1. Dependencies

The project works with Python version ``3.11.4``. More recent versions produce errors related to the 
project requirements.

To ensure the proper functioning of the project, it is necessary to have the appropriate versions of the 
tools described in the ``Requirements.txt`` file. 

You can install all the libraries using the following command:

``pip3 install -r requirements.txt``

After installing all the dependencies specified in the ``Requirements.txt`` file, 
it is necessary to execute the following command from the system terminal 
to install the ``es_core_news_sm`` dependency manually:

``python3 -m spacy download es_core_news_sm``

Additionally, it is necessary to install the ``sentence_transformers`` library 
manually using the following command:

``pip3 install -U sentence-transformers``

### 2.2. Environment Variables

The project uses environment variables defined in a ``.env`` file. 
You can use the example file ``.env.example`` to generate your own file that will contain the environment variables.



# CONTENEDOR DOCKER
Dockerfile

docker build -t fis-chatbot-api-main .
docker run -p 3000:3000 fis-chatbot-api-main


pyenv install 3.11.4

Si da error al instalar correr aparte el siguiente comando
pip install torch==2.1.0 --index-url https://pypi.org/simple
