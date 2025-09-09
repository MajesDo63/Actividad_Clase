# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo app.py al contenedor
COPY app.py .

# Comando que se ejecutará cuando inicie el contenedor
CMD ["python", "app.py"]
