# Projeto ETL com Python e IA Generativa

Este projeto foi desenvolvido com o objetivo de praticar os conceitos fundamentais de ETL (Extract, Transform, Load) utilizando Python.

O sistema simula um pipeline de dados bancários onde:

- os dados dos usuários são extraídos de um arquivo CSV
- as informações são transformadas através da geração de mensagens personalizadas sobre investimentos
- os dados são carregados novamente na estrutura da aplicação

---

# Objetivo do Projeto

Demonstrar na prática:

- leitura de arquivos CSV
- manipulação de dados com Pandas
- estruturas de dados em Python
- utilização de listas e dicionários
- integração com APIs de IA Generativa
- tratamento de erros com `try/except`
- fundamentos do processo ETL

---

# Tecnologias Utilizadas

- Python 3
- Pandas
- Google Gemini API
- OpenAI API (opcional)

---

# Estrutura do Projeto

```bash
Dio-pipepline-etl/
│
├── .venv/
├── .gitignore
├── ETL_Projetc.py
├── SDW2023.csv
└── README.md
```

---

# Como Funciona o ETL

## 1. Extract (Extração)

Os dados dos usuários são extraídos de um arquivo CSV utilizando Pandas.

```python
users = pd.read_csv('SDW2023.csv').to_dict(orient='records')
```

O método:

```python
to_dict(orient='records')
```

converte cada linha do CSV em um dicionário Python.

Exemplo:

```python
[
    {
        "Nome": "Felipe",
        "Conta": "0001-1",
        "Cartao": "1111"
    }
]
```

---

## 2. Transform (Transformação)

Nesta etapa:

- cada usuário recebe uma nova chave chamada `news`
- mensagens personalizadas são geradas
- os dados são enriquecidos
- erros são tratados utilizando `try/except`

Exemplo:

```python
for i in users:
    i['news'] = []
```

Adicionando mensagens:

```python
i['news'].append(gerar_mensagem(i))
```

---

## 3. Load (Carregamento)

Os dados transformados são armazenados novamente dentro da própria estrutura do sistema.

Exemplo final:

```python
{
    "Nome": "Felipe",
    "Conta": "0001-1",
    "Cartao": "1111",
    "news": [
        "Felipe, investir hoje é cuidar do seu futuro financeiro!"
    ]
}
```

---

# Tratamento de Erros

O projeto utiliza `try/except` para evitar que falhas externas interrompam o pipeline.

Exemplo:

```python
try:
    # chamada da API
except Exception as e:
    print(e)
```

Caso a API falhe:
- o sistema continua funcionando
- uma mensagem padrão é utilizada

---

# Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

---

## 2. Criar ambiente virtual

```bash
python -m venv .venv
```

---

## 3. Ativar o ambiente virtual

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

## 4. Instalar dependências

```bash
pip install pandas google-genai
```

---

## 5. Executar o projeto

```bash
python ETL_Projetc.py
```

---

# Arquivo .gitignore

O projeto utiliza `.gitignore` para evitar o envio de arquivos desnecessários ao GitHub.

Exemplo:

```gitignore
.venv/
__pycache__/
*.pyc
```

---

# Observações

Durante o desenvolvimento, foram utilizados modelos de IA Generativa como:
- Gemini

Entretanto, APIs podem apresentar:
- limites gratuitos
- indisponibilidade
- erros de quota
- falhas temporárias

Por isso o projeto implementa fallback utilizando mensagens locais.

---

# Aprendizados

Com este projeto foi possível praticar:

- fundamentos de ETL
- manipulação de CSV
- listas e dicionários
- integração com APIs
- tratamento de exceções
- organização de projetos Python
- Git e GitHub

---

# Autor

Projeto desenvolvido por Felipe Zimmermann para fins de estudo e prática de ETL com Python e IA Generativa.
