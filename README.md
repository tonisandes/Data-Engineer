# 🚀 Pipeline ETL com Python - Projeto de Portfólio

Este projeto simula um **pipeline de Engenharia de Dados (ETL)** simples, mas realista, usando **Python** e boas práticas de desenvolvimento. Ele extrai dados de uma API pública, transforma com Pandas e carrega em um banco de dados local.

Ideal para quem está começando na área de dados e quer demonstrar habilidades práticas de **extração, transformação e carga (ETL)**.
## 🔁 Funcionalidades do Pipeline

1. **Extract (Extração)**
   - Busca dados de usuários da API pública: [JSONPlaceholder](https://jsonplaceholder.typicode.com/users)
   - Salva os dados brutos em `data/raw/users_raw.json`

2. **Transform (Transformação)**
   - Limpa e estrutura os dados aninhados (endereço, empresa)
   - Remove duplicatas e trata campos nulos
   - Salva os dados limpos em formato **Parquet** (`data/processed/users_processed.parquet`)

3. **Load (Carga)**
   - Carrega os dados processados em um banco **SQLite** (`data/users.db`)
   - Tabela: `users`

---
