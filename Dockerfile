# Use a imagem oficial do Python como base
FROM python:3.11-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY . /app/

# Instale as dependências do sistema
RUN apt-get update && apt-get install -y libpq-dev

# Instale o pipenv e as dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponha a porta em que o servidor Django vai rodar
EXPOSE 8000

# Defina o comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
