# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл с кодом в рабочую директорию
COPY calculatorj.py .

# Указываем команду, которая будет выполнена при запуске контейнера
CMD ["python", "calculatorj.py"]
