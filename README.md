# 📊 Ciência de Dados e Coleta de Dados com Python

Este repositório contém scripts e estudos práticos sobre **Coleta de Dados (Data Collection)** e **Manipulação de Dados** utilizando Python. O objetivo é explorar técnicas de Web Scraping, consumo de APIs e estruturação de dados com Pandas.

## 🚀 Tecnologias Utilizadas

* **Python 3.14**
* **Pandas** (Manipulação de DataFrames e análise tabular)
* **Requests** (Requisições HTTP para APIs e Web)
* **BeautifulSoup4** (Extração de dados HTML / Web Scraping)

## 📂 Estrutura do Projeto

### 1. Coleta de Dados via Web (Web Scraping)
Arquivo: `coleta_dados_web.py`
* Exploração da estrutura HTML (DOM).
* Navegação entre tags **Pai, Filho e Irmãos (Siblings)**.
* Extração de títulos e links de notícias do site *python.org.br*.
* Uso de `find`, `find_all` e `find_next_siblings`.

### 2. Consumo de API (Automação)
Arquivo: `coleta_dados_api.py`
* Integração com a API do **Gofile.io**.
* Upload de arquivos (PDF) via requisições `POST`.
* Manipulação de respostas **JSON**.
* Tratamento de erros (`try/except`) e verificação de status HTTP.

### 3. Manipulação de Dados (Data Science)
Arquivo: `estudo_dataframe_ciencias.py`
* Criação de **DataFrames** a partir de dicionários.
* Seleção de dados com **`loc`** e **`iloc`**.
* Filtragem de dados (ex: idade > 21).
* Limpeza de dados (remoção de colunas com `drop`).
* Leitura e escrita de arquivos **CSV**.

## 📦 Como Executar

Certifique-se de ter as bibliotecas instaladas:

```bash
pip install pandas requests beautifulsoup4
