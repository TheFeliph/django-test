# Use uma imagem oficial do Python como base
FROM python:3.11-slim

# Set o diretório de trabalho
WORKDIR /app

# Copie os arquivos para o diretório de trabalho
COPY . /app/

# Instale as dependências
RUN apt-get update && apt-get install -y libpq-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponha a porta 8000 para o Django
EXPOSE 8000

# Defina o comando de inicialização
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
