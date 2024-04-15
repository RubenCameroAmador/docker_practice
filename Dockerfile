# Usa una imagen de Python oficial como base
FROM python:3.11.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt para instalar las dependencias de la aplicación
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación al contenedor
COPY . /app/

# Expone el puerto en el que se ejecuta la aplicación Flask
EXPOSE 9999

# Comando para ejecutar la aplicación Flask
CMD ["python", "main.py"]