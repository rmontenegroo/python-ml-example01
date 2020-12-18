# python-ml-example01

### 2 Modelos de árvores de decisão expostos através de uma API escrita em python utilizando Flask

## Modos de input:

* *json payload*

* upload de csv por cliente HTTP

* upload de csv por submissão de formulário HTML

## Porta: 8080

## Python 3.8+

## Formas de execução da aplicação

### Execução pelo python local

Uma vez que tenha o python e o pip instalados no computador, você pode seguir os seguintes passos:

    1. pip install -r requirements.txt;
    2. python app.py

### Execução em container [Docker](https://www.docker.com/)

Num computador com linux e o docker instalado, simplesmente execute:

`make run`

O docker irá fazer o build da imagem, e em seguida irá subir a aplicação na porta 8080.

Qualquer que seja o caminho escolhido para a execução, ao final do procedimento, abra um navegador e acesse [http://localhost:8080/](http://localhost:8080).