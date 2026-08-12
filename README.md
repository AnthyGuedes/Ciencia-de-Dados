# 📊 Ciência de Dados e Coleta de Dados com Python

Este repositório contém scripts e estudos práticos sobre **Coleta de Dados (Data Collection)**, **Web Scraping**, **Consumo de APIs** e **Manipulação de Dados** utilizando Python.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.14+**
* **Pandas** (Manipulação de DataFrames, análise e exportação tabular)
* **Requests** (Requisições HTTP para consumo de APIs e Web)
* **BeautifulSoup4** (Extração e manipulação de dados HTML / Web Scraping)
* **Faker** (Geração de dados fictícios para testes em português)

---

## 📚 Ordem das Aulas e Explicação dos Códigos

Abaixo está a sequência recomendada de estudo, detalhando o objetivo e os conceitos abordados em cada arquivo do projeto:

### 1️⃣ Fundamentos e Fatiamento de Dados
📄 **Arquivo:** [`estudo.py`](file:///c:/EBAC_Ciencia_Dados_Repo/Ciencia-de-Dados/estudo.py)
* **Conceito:** Conceito básico de fatiamento (*slicing*) de listas e strings em Python.
* **Resumo:** Demonstra o uso de limites de intervalo (ex: `texto[:11]` e `texto[8:]`), utilizado para truncar a exibição de respostas extensas de requisições HTTP (`response.text[:600]`).

---

### 2️⃣ Coleta de Dados Básica (Web & Tabelas)
📄 **Arquivo:** [`coleta_dados_basica.py`](file:///c:/EBAC_Ciencia_Dados_Repo/Ciencia-de-Dados/coleta_dados_basica.py)
* **Conceito:** Introdução à requisição de dados web e extração de tabelas.
* **Resumo:**
  * Realiza requisições HTTP brutas com `requests.get()`.
  * Formata e analisa a estrutura HTML com `BeautifulSoup` (`prettify()`).
  * Utiliza `pandas.read_html()` para converter diretamente tabelas HTML (`<table>`) de sites em **DataFrames**.

---

### 3️⃣ Web Scraping Avançado e Navegação DOM
📄 **Arquivo:** [`coleta_dados_web.py`](file:///c:/EBAC_Ciencia_Dados_Repo/Ciencia-de-Dados/coleta_dados_web.py)
* **Conceito:** Raspagem de dados estruturados e navegação na árvore DOM.
* **Resumo:**
  * Filtragem de múltiplas tags HTML (`find_all(['h1', 'h2'])`) com contagem de ocorrências.
  * Extração de links aninhados em tags (`<h3>` e `<a>`).
  * Navegação entre elementos vizinhos no DOM utilizando `find_next_siblings` com busca flexível (`<p>`, `<div>`, `<ul>`).

---

### 4️⃣ Consumo de API REST e Envio de Arquivos
📄 **Arquivo:** [`coleta_dados_api.py`](file:///c:/EBAC_Ciencia_Dados_Repo/Ciencia-de-Dados/coleta_dados_api.py)
* **Conceito:** Interação com APIs externas via métodos `POST` e `GET`.
* **Resumo:**
  * Upload de arquivos em modo binário (`rb`) para a API do *Gofile.io*.
  * Envio de requisições com autenticação via cabeçalhos (`Authorization` API Key).
  * Leitura e manipulação da resposta em formato `JSON`.
  * Download automático de arquivos a partir de URLs recebidas.

---

### 5️⃣ Consumo Avançado de API e Tratamento de Erros
📄 **Arquivo:** [`coleta_dados_api_server.py`](file:///c:/EBAC_Ciencia_Dados_Repo/Ciencia-de-Dados/coleta_dados_api_server.py)
* **Conceito:** Especificação de endpoints de servidores, resiliência e tratamento de exceções.
* **Resumo:**
  * Upload direcionado a servidores específicos (`store1.gofile.io/contents/uploadfile`).
  * Definição de `timeout` para prevenção de travamentos.
  * Tratamento estruturado de erros com `try / except` (`JSONDecodeError`, `FileNotFoundError`).

---

### 6️⃣ Manipulação e Análise de DataFrames
📄 **Arquivo:** [`estudo_dataframe_ciencias.py`](file:///c:/EBAC_Ciencia_Dados_Repo/Ciencia-de-Dados/estudo_dataframe_ciencias.py)
* **Conceito:** Operações fundamentais com Pandas.
* **Resumo:**
  * Criação de DataFrames a partir de dicionários e listas de dicionários.
  * Seleção de colunas e indexação com `iloc` e `loc`.
  * Adição e remoção de colunas (`drop`) e novos registros.
  * Filtragem condicional (ex: `df['idade'] >= 21`).
  * Exportação (`to_csv`) e leitura (`read_csv`) de arquivos CSV.

---

### 7️⃣ Geração de Dados Fictícios para Testes
📄 **Arquivo:** [`gerar_dados.py`](file:///c:/EBAC_Ciencia_Dados_Repo/Ciencia-de-Dados/gerar_dados.py)
* **Conceito:** Criação automatizada de conjuntos de dados sintéticos.
* **Resumo:**
  * Utiliza a biblioteca `Faker` (localização `pt_BR`) para gerar nomes, CPFs, datas e endereços brasileiros.
  * Combina com o módulo `random` para geração de idades aleatórias.
  * Ajusta configurações de exibição do Pandas (`display.max_columns`, `display.width`).
  * Gera e salva a base no arquivo `clientes.csv`.

---

## 📦 Como Executar

### 1. Instalar as Dependências
No terminal, execute:

```bash
pip install pandas requests beautifulsoup4 faker
```

### 2. Executar um Script Específico
Para rodar qualquer uma das aulas, navegue até a pasta e execute:

```bash
python <nome_do_arquivo>.py
```

Exemplo:
```bash
python coleta_dados_web.py
```
