# 📊 Ciência de Dados com Python: Da Coleta ao Tratamento

Repositório dedicado ao estudo prático e estruturado de **Ciência de Dados** utilizando **Python**. O projeto abrange as principais etapas do ciclo inicial de engenharia e análise de dados: **Coleta de Dados (Web Scraping e Consumo de APIs)**, **Limpeza e Higienização**, **Tratamento e Transformação**, **Fundamentos de Manipulação Tabular com Pandas** e **Geração de Dados Sintéticos**.

---

## 📌 Sumário

* [🚀 Tecnologias e Bibliotecas](#-tecnologias-e-bibliotecas)
* [📂 Mapa de Códigos por Categoria](#-mapa-de-códigos-por-categoria)
* [🌐 1. Coleta de Dados & Web Scraping](#-1-coleta-de-dados--web-scraping)
* [🧹 2. Limpeza de Dados (Data Cleaning)](#-2-limpeza-de-dados-data-cleaning)
* [⚙️ 3. Tratamento e Transformação de Dados](#-3-tratamento-e-transformação-de-dados)
* [📊 4. Fundamentos e Manipulação de Dados](#-4-fundamentos-e-manipulação-de-dados)
* [🎲 5. Geração de Dados Sintéticos](#-5-geração-de-dados-sintéticos)
* [📁 6. Bases de Dados e Datasets](#-6-bases-de-dados-e-datasets)
* [🌳 Estrutura de Diretórios](#-estrutura-de-diretórios)
* [💻 Como Executar o Projeto](#-como-executar-o-projeto)
* [💡 Boas Práticas Abordadas](#-boas-práticas-abordadas)

---

## 🚀 Tecnologias e Bibliotecas

| Tecnologia / Lib | Versão Sugerida | Finalidade no Repositório |
| :--- | :--- | :--- |
| **Python** | `3.10+` | Linguagem base para desenvolvimento de todos os scripts |
| **Pandas** | `^2.0` | Criação, inspeção, fatiamento, filtros, I/O e manipulação de DataFrames |
| **Requests** | `^2.31` | Requisições HTTP (GET, POST), upload binário de arquivos e integração com APIs |
| **BeautifulSoup4** | `^4.12` | Extração, navegação e raspagem de dados HTML (DOM / Web Scraping) |
| **Faker** | `^24.0` | Geração de dados sintéticos e fictícios no padrão brasileiro (`pt_BR`) |
| **lxml / html5lib** | `^5.0` | Parsers utilizados pelo Pandas para extração com `read_html()` |

---

## 📂 Mapa de Códigos por Categoria

A tabela abaixo resume todos os códigos do repositório organizados por assunto principal:

| Categoria | Arquivo | Descrição Resumida |
| :--- | :--- | :--- |
| **🌐 Coleta de Dados** | [`coleta_dados_basica.py`](./coleta_dados_basica.py) | Extração direta de tabelas HTML para DataFrames com `read_html()` e BeautifulSoup. |
| **🌐 Coleta de Dados** | [`coleta_dados_web.py`](./coleta_dados_web.py) | Scraping avançado de elementos HTML, busca aninhada e navegação DOM por vizinhança. |
| **🌐 Coleta de Dados** | [`coleta_dados_api.py`](./coleta_dados_api.py) | Consumo de API REST, upload binário de arquivos, headers de autenticação e download. |
| **🌐 Coleta de Dados** | [`coleta_dados_api_server.py`](./coleta_dados_api_server.py) | Upload resiliente em API com seleção de servidor, `timeout` e tratamento de exceções. |
| **🧹 Limpeza de Dados** | [`Tratamento-de-Dados/limpeza_dados.py`](./Tratamento-de-Dados/limpeza_dados.py) | Higienização de bases: eliminação de colunas (`axis=1`) e exclusão de linhas (`axis=0`). |
| **⚙️ Tratamento de Dados** | [`Tratamento-de-Dados/intro_tratamento_dados.py`](./Tratamento-de-Dados/intro_tratamento_dados.py) | Diagnóstico exploratório: checagem dimensional (`shape`), tipagem (`dtypes`) e valores nulos. |
| **⚙️ Tratamento de Dados** | [`Tratamento-de-Dados/estudo_lambda.py`](./Tratamento-de-Dados/estudo_lambda.py) | Transformação de dados com funções nomeadas (`def`) vs funções anônimas (`lambda`) via `.apply()`. |
| **📊 Manipulação & Fundamentos**| [`estudo.py`](./estudo.py) | Conceito de fatiamento de sequências (*slicing*) para controle de payloads de requisições. |
| **📊 Manipulação & Fundamentos**| [`estudo_dataframe_ciencias.py`](./estudo_dataframe_ciencias.py) | Operações completas de DataFrame: `loc`/`iloc`, inclusão de dados, filtros lógicos e I/O CSV. |
| **🎲 Dados Sintéticos** | [`gerar_dados.py`](./gerar_dados.py) | Criação de base fictícia brasileira (`Faker pt_BR`), geração de CPFs e exportação para CSV. |

---

## 🌐 1. Coleta de Dados & Web Scraping

Nesta categoria estão os scripts responsáveis por capturar informações externas a partir de páginas web estáticas, árvores de elementos HTML e endpoints de APIs RESTful.

### 📄 [`coleta_dados_basica.py`](./coleta_dados_basica.py)
* **Objetivo:** Introdução à requisição de conteúdo web e conversão automática de tabelas HTML.
* **Técnicas Abordadas:**
  * Realização de requisição HTTP direta com `requests.get()`.
  * Formatação e estruturação visual do código HTML com `BeautifulSoup(..., 'html.parser')` e `.prettify()`.
  * Uso do método `pandas.read_html()` para identificar automaticamente tags `<table>` em páginas web e transformá-las diretamente em DataFrames prontos para análise.

### 📄 [`coleta_dados_web.py`](./coleta_dados_web.py)
* **Objetivo:** Raspagem estruturada e navegação avançada na árvore DOM (*Document Object Model*) utilizando o site [Python Brasil](https://python.org.br/).
* **Técnicas Abordadas:**
  * Filtragem múltipla de tags simultaneamente (`extracao.find_all(['h1', 'h2'])`) com contagem quantitativa de títulos.
  * Captura de elementos aninhados (extração de links `<a>` contidos dentro de títulos `<h3>`).
  * Navegação entre elementos irmãos/vizinhos utilizando `find_next_siblings` com busca flexível (`p`, `ul`, `div`), permitindo extrair resumos e hyperlinks de maneira dinâmica.

### 📄 [`coleta_dados_api.py`](./coleta_dados_api.py)
* **Objetivo:** Integração com APIs externas para transferência de arquivos e consumo de payloads JSON.
* **Técnicas Abordadas:**
  * Upload de arquivos em formato binário (`open(..., 'rb')`) através do método HTTP `POST` utilizando o serviço *Gofile.io*.
  * Configuração de cabeçalhos de autenticação via headers (`Authorization` com API Key).
  * Desserialização da resposta do servidor com `response.json()`.
  * Implementação de função para download automático de arquivos a partir de URLs com `requests.get()` gravando em modo binário (`'wb'`).

### 📄 [`coleta_dados_api_server.py`](./coleta_dados_api_server.py)
* **Objetivo:** Consumo resiliente de APIs com foco em tolerância a falhas e tratamento de exceções.
* **Técnicas Abordadas:**
  * Roteamento direcionado para endpoints de servidores específicos (`store1.gofile.io/contents/uploadfile`).
  * Aplicação de `timeout=60` nas requisições HTTP para evitar que a aplicação congele em caso de instabilidade na rede.
  * Tratamento de falhas estruturado com `try / except`:
    * Captura de `requests.exceptions.JSONDecodeError` quando a API retorna HTML ou resposta truncada.
    * Captura de `FileNotFoundError` para validação prévia de caminhos de arquivos locais.

---

## 🧹 2. Limpeza de Dados (Data Cleaning)

A etapa de limpeza foca na eliminação de redundâncias, correção de irregularidades e remoção de registros e atributos desnecessários para a análise.

### 📄 [`Tratamento-de-Dados/limpeza_dados.py`](./Tratamento-de-Dados/limpeza_dados.py)
* **Objetivo:** Aplicação prática de remoção de colunas e registros em DataFrames do Pandas.
* **Técnicas Abordadas:**
  * **Exclusão de Colunas:** Utilização de `df.drop('pais', axis=1, inplace=True)` para eliminar atributos constantes ou desnecessários.
  * **Exclusão de Linhas por Índice:** Utilização de `df.drop(2, axis=0, inplace=True)` para descartar registros específicos.
  * **Configuração de Exibição:** Uso de `pd.set_option('display.width', None)` para permitir a visualização completa do DataFrame no terminal sem truncamento lateral.

---

## ⚙️ 3. Tratamento e Transformação de Dados

Esta categoria reúne scripts dedicados ao diagnóstico de qualidade de bases de dados e aplicação de funções de transformação vetorizada em colunas.

### 📄 [`Tratamento-de-Dados/intro_tratamento_dados.py`](./Tratamento-de-Dados/intro_tratamento_dados.py)
* **Objetivo:** Inspeção exploratória inicial, diagnóstico estrutural e auditoria de qualidade da base `clientes.csv`.
* **Técnicas Abordadas:**
  * Inspeção amostral de início e fim da base com `df.head()` e `df.tail()`.
  * Verificação volumétrica e dimensional do dataset com `df.shape` (quantidade de linhas e colunas).
  * Auditoria de tipos de dados de cada coluna com `df.dtypes`.
  * Diagnóstico de valores ausentes/nulos por coluna com `df.isnull().sum()`.

### 📄 [`Tratamento-de-Dados/estudo_lambda.py`](./Tratamento-de-Dados/estudo_lambda.py)
* **Objetivo:** Aplicação e comparação prática entre funções nomeadas (`def`) e expressões anônimas (`lambda`) na transformação de dados tabulares.
* **Técnicas Abordadas:**
  * Definição de funções matemáticas tradicionais (`def eleva_cubo(x)`).
  * Criação de expressões anônimas com sintaxe concisa: `lambda x: x ** 3`.
  * Mapeamento vetorizado de colunas através do método `.apply()` do Pandas:
    * `df['cubo_funcao'] = df['números'].apply(eleva_cubo)`
    * `df['cubo_lambda'] = df['números'].apply(lambda x: x ** 3)`
  * **Regra prática:** Utilização de `lambda` para transformações pontuais e simples; adoção de funções tradicionais com `def` para operações complexas, validações e regras de negócio que necessitem de manutenção e documentação.

---

## 📊 4. Fundamentos e Manipulação de Dados

Reúne conceitos essenciais de estruturas de dados em Python e a base fundamental para operar com o Pandas.

### 📄 [`estudo.py`](./estudo.py)
* **Objetivo:** Compreensão da mecânica de fatiamento (*slicing*) de sequências numéricas e de texto.
* **Técnicas Abordadas:**
  * Aplicação de limites de início e fim: `sequencia[:11]` e `sequencia[8:]`.
  * Base fundamental para truncamento de payloads extensos recebidos em respostas de rede (ex: `response.text[:600]`).

### 📄 [`estudo_dataframe_ciencias.py`](./estudo_dataframe_ciencias.py)
* **Objetivo:** Guia completo de manipulação bidimensional com Pandas.
* **Técnicas Abordadas:**
  * Conversão de estruturas nativas (listas e listas de dicionários) em DataFrames.
  * Indexação e seleção de dados com `.iloc[]` (por índice inteiro) e `.loc[]` (por rótulo/posição).
  * Seleção univariada (`df['coluna']`) e multivariada (`df[['col1', 'col2']]`).
  * Adição de novas colunas com valores e inserção de novos registros com `.loc[len(df)]`.
  * Filtragem condicional booleana (ex: `df[df['idade'] >= 21]`).
  * Persistência de dados: exportação para CSV com `df.to_csv('dados.csv', index=False)` e importação com `pd.read_csv()`.

---

## 🎲 5. Geração de Dados Sintéticos

### 📄 [`gerar_dados.py`](./gerar_dados.py)
* **Objetivo:** Geração automatizada de datasets sintéticos com dados realistas para simulação, testes de carga e rotinas de ETL.
* **Técnicas Abordadas:**
  * Utilização da biblioteca `Faker` com localização brasileira (`Faker('pt_BR')`).
  * Geração de nomes completos, números de CPF válidos no padrão nacional, datas de nascimento e endereços com estados.
  * Uso do módulo `random` (`random.randint(18, 60)`) para compor idades aleatórias compatíveis com a data de nascimento.
  * Ajustes avançados nas opções de exibição do Pandas (`display.max_columns`, `display.max_rows`, `display.max_colwidth`, `display.width`).
  * Exportação automatizada da base gerada para `clientes.csv`.

---

## 📁 6. Bases de Dados e Datasets

* **`clientes.csv` / `Tratamento-de-Dados/clientes.csv`:**
  * Dataset sintético contendo cadastros de clientes (Nome, CPF, Idade, Endereço, Estado e País).
  * Utilizado como fonte de dados para as aulas e práticas de diagnóstico (`intro_tratamento_dados.py`) e limpeza (`limpeza_dados.py`).
* **`dados.csv`:**
  * Arquivo CSV gerado a partir do script `estudo_dataframe_ciencias.py` demonstrando a persistência e posterior leitura de dados manipulados com Pandas.

---

## 🌳 Estrutura de Diretórios

```text
Ciencia-de-Dados/
│
├── 📁 Tratamento-de-Dados/
│   ├── clientes.csv                     # Base de clientes para testes de tratamento
│   ├── estudo_lambda.py                 # [Tratamento] Funções anônimas e .apply()
│   ├── intro_tratamento_dados.py        # [Tratamento] Diagnóstico de nulos e tipos
│   └── limpeza_dados.py                 # [Limpeza] Remoção de colunas e linhas
│
├── clientes.csv                         # Base de clientes gerada pelo Faker
├── coleta_dados_api.py                  # [Coleta] Consumo de API REST, upload/download
├── coleta_dados_api_server.py           # [Coleta] Upload em API com timeout e try/except
├── coleta_dados_basica.py               # [Coleta] Web scraping básico e read_html()
├── coleta_dados_web.py                  # [Coleta] Scraping avançado e navegação no DOM
├── dados.csv                            # Base CSV de teste gerada no estudo
├── estudo.py                            # [Fundamentos] Fatiamento (slicing) de dados
├── estudo_dataframe_ciencias.py         # [Manipulação] Operações fundamentais em DataFrames
├── gerar_dados.py                       # [Geração] Criação de dados sintéticos (Faker)
└── README.md                            # Documentação completa do repositório
```

---

## 💻 Como Executar o Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/AnthyGuedes/Ciencia-de-Dados.git
cd Ciencia-de-Dados
```

### 2. Criar e Ativar um Ambiente Virtual (Opcional, mas Recomendado)

* **No Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```

* **No Linux / macOS:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Instalar as Dependências

```bash
pip install pandas requests beautifulsoup4 faker lxml
```

### 4. Executando os Scripts por Assunto

* **Para gerar a base de clientes fictícios:**
  ```bash
  python gerar_dados.py
  ```

* **Para testar coleta web e scraping:**
  ```bash
  python coleta_dados_basica.py
  python coleta_dados_web.py
  ```

* **Para testar consumo de APIs:**
  ```bash
  python coleta_dados_api.py
  python coleta_dados_api_server.py
  ```

* **Para rotinas de tratamento e limpeza de dados:**
  ```bash
  python Tratamento-de-Dados/intro_tratamento_dados.py
  python Tratamento-de-Dados/limpeza_dados.py
  python Tratamento-de-Dados/estudo_lambda.py
  ```

* **Para fundamentos de manipulação com Pandas:**
  ```bash
  python estudo_dataframe_ciencias.py
  ```

---

## 💡 Boas Práticas Abordadas

1. **Robustez em Requisições Web:** Sempre configure o parâmetro `timeout` em chamadas HTTP com `requests` para prevenir travamento indefinido do processo por indisponibilidade do servidor.
2. **Tratamento Específico de Exceções:** Trate erros esperados individualmente (`requests.exceptions.JSONDecodeError`, `FileNotFoundError`) antes de capturar exceções genéricas (`Exception`).
3. **Navegação Semântica no DOM:** Ao fazer web scraping, utilize seletores relativos como `find_next_siblings` com listas de tags alternativas para criar scrapers mais resilientes a mudanças visuais no site.
4. **Vetorização vs Loops:** Em Pandas, dê preferência a operações vetorizadas e ao método `.apply()` em vez de iterar sobre linhas com loops `for`.
5. **Auditoria Prévia de Dados:** Antes de iniciar qualquer limpeza ou modelagem, sempre verifique dimensões (`.shape`), tipos de dados (`.dtypes`) e contagem de nulos (`.isnull().sum()`).
