import pandas as pd
import random
import os

from faker import Faker
from datetime import datetime, timedelta


# ==========================================
# CONFIGURAÇÕES INICIAIS
# ==========================================

fake = Faker("pt_BR")

# Quantidade inicial de vendas para teste
quantidade_vendas = 100


# ==========================================
# DADOS DA EMPRESA
# ==========================================

produtos = [
    {
        "produto": "Notebook Gamer",
        "categoria": "Tecnologia",
        "valor": 5500,
        "custo": 4200
    },
    {
        "produto": "Smartphone",
        "categoria": "Tecnologia",
        "valor": 3000,
        "custo": 2200
    },
    {
        "produto": "Tablet",
        "categoria": "Tecnologia",
        "valor": 1800,
        "custo": 1200
    },
    {
        "produto": "Monitor",
        "categoria": "Tecnologia",
        "valor": 1200,
        "custo": 800
    },
    {
        "produto": "Mouse",
        "categoria": "Acessórios",
        "valor": 150,
        "custo": 50
    },
    {
        "produto": "Teclado Mecânico",
        "categoria": "Acessórios",
        "valor": 350,
        "custo": 150
    },
    {
        "produto": "Headset",
        "categoria": "Acessórios",
        "valor": 450,
        "custo": 250
    },
    {
        "produto": "SSD 1TB",
        "categoria": "Informática",
        "valor": 600,
        "custo": 350
    }
]


cidades = [
    {
        "cidade": "São Paulo",
        "estado": "SP"
    },
    {
        "cidade": "Rio de Janeiro",
        "estado": "RJ"
    },
    {
        "cidade": "Curitiba",
        "estado": "PR"
    },
    {
        "cidade": "Belo Horizonte",
        "estado": "MG"
    },
    {
        "cidade": "Brasília",
        "estado": "DF"
    }
]


formas_pagamento = [
    "Cartão de Crédito",
    "Pix",
    "Boleto",
    "Cartão de Débito"
]


canais_venda = [
    "Online",
    "Loja Física",
    "Marketplace"
]


# ==========================================
# GERAÇÃO DAS VENDAS
# ==========================================

vendas = []


data_inicio = datetime(2025, 1, 1)

data_fim = datetime(2026, 12, 31)


for i in range(quantidade_vendas):

    produto = random.choice(produtos)

    cidade = random.choice(cidades)

    quantidade = random.randint(1, 5)


    data_venda = data_inicio + timedelta(
        days=random.randint(
            0,
            (data_fim - data_inicio).days
        )
    )


    valor_total = produto["valor"] * quantidade

    custo_total = produto["custo"] * quantidade

    lucro = valor_total - custo_total


    venda = {

        "id_venda": i + 1,

        "data_venda": data_venda.strftime("%Y-%m-%d"),

        "cliente": fake.name(),

        "produto": produto["produto"],

        "categoria": produto["categoria"],

        "quantidade": quantidade,

        "valor_unitario": produto["valor"],

        "custo_unitario": produto["custo"],

        "valor_total": valor_total,

        "custo_total": custo_total,

        "lucro": lucro,

        "cidade": cidade["cidade"],

        "estado": cidade["estado"],

        "forma_pagamento": random.choice(formas_pagamento),

        "canal_venda": random.choice(canais_venda)

    }


    vendas.append(venda)



# ==========================================
# CRIAÇÃO DO DATAFRAME
# ==========================================

df = pd.DataFrame(vendas)



# ==========================================
# SALVAMENTO DO ARQUIVO CSV
# ==========================================

diretorio_atual = os.path.dirname(__file__)


pasta_saida = os.path.join(
    diretorio_atual,
    "../data"
)


os.makedirs(
    pasta_saida,
    exist_ok=True
)


arquivo_csv = os.path.join(
    pasta_saida,
    "vendas.csv"
)



df.to_csv(
    arquivo_csv,
    index=False,
    encoding="utf-8"
)



# ==========================================
# VALIDAÇÃO
# ==========================================

print("===================================")
print("Arquivo vendas.csv criado com sucesso!")
print("===================================")

print(f"Quantidade de vendas geradas: {len(df)}")

print("\nPrimeiros registros:")
print(df.head())