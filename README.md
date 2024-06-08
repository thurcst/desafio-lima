# Projeto Lima

## Desafio

Objetivo principal é **Coletar e armazenar dados de Notícias**

De forma que a solução forneça os seguintes serviços:

-   Extrai dados de um site de notícias
-   Limpa os dados
-   Armazenar os dados no BigQuery (Bônus)
-   Expõe os dados via API

### Objetivo

-   Avaliar habilidades com programação
-   Entender o nível técnico
-   Entender como ocorre o processo de design de solução

### Critérios

-   Padrão de código
-   Padrão de commits
-   Estilo
-   Solução desenvolvida
-   Uso apropriado de `source control`

### Instruções

Write an application to crawl an online news website, e.g. www.theguardian.com/au or www.bbc.com using a crawler framework such as [Scrapy] (http://scrapy.org/).
You can use a crawl framework of your choice and build the application in Python.

The appliction should cleanse the articles to obtain only information relevant to the news story, e.g. article text, author, headline, article url, etc. Use a framework such as Readability to cleanse the page of superfluous content such as advertising and html

## Execução

### Site escolhido

Após alguns testes em outras aplicações, escolhi o site da [Adrenaline] (https://www.adrenaline.com.br/) como fonte dos artigos.

_Ah, mas por quê?_ Você pode estar se perguntando. E a resposta é simples mas pode ser dividida em 3 principais motivos:

-   Organização do site
    -   O site possui uma estrutura que é favorável para a extração, com padrões de estrutura HTML bem definidos. Dados como autor, data, categorias e outras informações são simples de encontrar.
    -   O site da Adrenaline possui várias sessões de diferentes tipos de notícias, então pude fazer um `spider` pra cada tipo.
    -   `robots.txt`... Acho que essa parte foi a mais chata. O Adrenaline permite extrair dados da primeira página de notícias, o que limitou um pouco a quantidade de notícias e a profundidade em que poderia chegar com o crawler, mas como são várias sessões, acaba que não faz muita diferença no fim. Há uma quantidade considerável de artigos e isso já me deixou bem satisfeito.

### Dificuldades

No meu dia a dia não faço uso de web scrapping no contexto em que trabalho. Então, aprender a utilizar a lib `scrapy` foi o que mais tomou meu tempo. A integração com Big Query e o servidor foram as partes menos trabalhosas do processo, mas também precisaram de bastante atenção (principalmente em relação a documentação).

### Lista de tarefas

-   [x] Revisar conteúdos sobre Web Scrapping
-   [x] (2024/06/07) Criação de Spiders
    -   [x] (2024/06/07) Artigos
    -   [x] (2024/06/07) Notícias
    -   [x] (2024/06/08) Análises
-   [x] (2024/06/08) Armazenamento no Big Query
-   [x] (2024/06/08) Leitura do Big Query
-   [x] (2024/06/08) Criação da API
-   [x] (2024/06/08) Integração do BigQuery na API
