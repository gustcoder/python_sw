# Python - Teste com API SWAPI
<b>Link:</b> https://swapi.dev/

![Badge API](http://img.shields.io/static/v1?label=API&message=SWAPI&color=GREEN&style=for-the-badge)
![Badge Python](http://img.shields.io/static/v1?label=PYTHON&message=V.3&color=blue&style=for-the-badge)
![Badge Docker](http://img.shields.io/static/v1?label=DOCKER&message=Container&color=blue&style=for-the-badge)

![image](https://github.com/gustcoder/python_sw/assets/52874054/ab12af76-766d-4069-8902-7facd845c96e)

<h1> Descrição </h1>

A SWAPI é uma API bem simples e interessante que traz diversas informações interessantes sobre os filmes, personagens, planetas e demais dados sobre o clássico Star Wars!
E serve muito bem para o aprendizado sobre REST API, requests etc.

Este projeto tem como objetivo apenas fazer algumas requisições para esta API utilizando Python e alguns recursos do Pandas.

<h1> Pré-requisitos </h1>

* Docker versão 20 ou superior

<h1> Buildando o container </h1>
Após clonar o projeto, dentro do diretório principal, por favor execute o seguinte comando:

```docker build -t python-sw .```

<h1> Executando script </h1>
Após ter buidado o container, vamos rodá-lo!

```docker run -it --rm --name python-sw-app python-sw```

<h1> Saída Esperada </h1>
O retorno esperado é aparecer esta lista de filmes ordenada pelo episódio:
![image](https://github.com/gustcoder/python_sw/assets/52874054/a71a683f-07e0-45e9-9587-22eff88ba270)


<b>Materiais de apoio</b>:

https://swapi.dev/documentation

https://pandas.pydata.org/docs/user_guide/index.html

https://hub.docker.com/_/python
