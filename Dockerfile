# 1. Use uma imagem oficial e leve do Python
FROM python:3.11-slim

# 2. Defina o diretório de trabalho
WORKDIR /app

# 3. Instale dependências do sistema necessárias
RUN apt-get update && apt-get install -y libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 4. Copie o arquivo de requisitos primeiro para aproveitar o cache
COPY requirements.txt .

# 5. Atualize o pip e instale dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# 6. Copie o restante do código do app
COPY . .

# 7. Comando padrão para rodar o app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
