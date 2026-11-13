# Usamos una imagen oficial ligera de Python
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos nuestro script al contenedor
COPY app.py /app/

# Exponemos el puerto 3000
EXPOSE 3000

# Ejecutamos el script de Python directamente
CMD ["python", "app.py"]
