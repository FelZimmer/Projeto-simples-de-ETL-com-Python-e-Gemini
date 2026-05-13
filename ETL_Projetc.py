# importar as bibliotecas necessárias 
import pandas as pd 
from google import genai
from google.genai import types

# Ler o arquivo CSV e converter para uma lista de dicionários, onde cada dicionário(registro) representa um usuário
users  = pd.read_csv('SDW2023.csv').to_dict(orient='records')

# Adicionar uma nova chave 'news' para cada usuário, que será usada para armazenar as mensagens personalizadas geradas para cada usuário
for i in users:
    i['news'] = []

# Inicializar o cliente da API do Gemini-2.0-flash usando a chave de API criada, mas como não é possível usar a API, essa parte do código está comentada
#client = genai.Client(api_key="sua_chave_api_aqui")

# Funcao para gerar mensagens personalizadas usando o modelo Gemini-2.0-flash mas se nao for possível, retorna uma mensagem padrão
def gerar_mensagem(user):

    try:
        # Gerar uma mensagem personalizada para o usuário usando o modelo Gemini-2.0-flash, mas como não é possível usar a API, essa parte do código está comentada
        #news = client.models.generate_content(

       #     model="gemini-2.0-flash",
        #    config=types.GenerateContentConfig(
       #         system_instruction="Você é um especialista em investimentos e finanças pessoais.",
       #         temperature=0.1,
       #     ),

       #     contents=f"Crie uma mensagem curta (máximo 100 caracteres) para {user['Nome']} sobre investimentos."
      #  )

       # return news.text
       return f"{user['Nome']}, investir hoje é cuidar do seu futuro financeiro!"

    except Exception as e:

        print(f"Erro ao gerar mensagem para {user['Nome']}: {e}")

        return f"{user['Nome']}, investir hoje é cuidar do seu futuro financeiro!"
    
#looping para gerar mensagens personalizadas para cada usuário e adicioná-las à lista de notícias de cada usuário, e imprimir a mensagem gerada

for i in users: 
    i['news'].append(gerar_mensagem(i))
    print(f"Mensagem para {i['Nome']}: {i['news']}")


