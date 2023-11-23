![LinkedIn e Selenium logos](https://github.com/Romano-g/Linkedin-Selenium/assets/143983377/d655eb4e-1afd-47bb-ab37-cac8fa6c39a7)

# Linkedin-Selenium
 
Neste repositório automatizei a função de adicionar pessoas e aumentar meu network no LinkedIn com o uso da biblioteca de WebScraping "Selenium", em conjunto com a linguagem Python.

## Funcionalidade:

A automação conta com tempos aleatórios entre os cliques de 1 a 5 segundos cada um, para se tornar mais natural, além disso essa automação realiza, em sequência:

* Login com os dados de e-mail e senha definidos pelo usuário;
* Pausa para que o usuário realize a captcha para confirmar que é humano;
* Pesquisa a área de atuação que o usuário definir;
* Filtra para conexões de segundo grau;
* Envia a solicitação de conexão junto a uma mensagem que o usuário definir.

Para ver a automação funcionando você pode [clicar aqui.](https://youtu.be/5rekbQEQFPI)

## .env

Para manter a privacidade dos usuários e minha, utilizei o método dotenv, segue exemplo da construção do dotenv:

~~~
EMAIL=''
SENHA=''
AREA=''
MSG=''
~~~

Caso deseje utilizar a automação, não se esqueca de usar `pip install -r requirements.txt` após baixar os arquivos para utilizar no seu editor.
