# Используем официальный образ Python
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /snt2

# Копируем зависимости и файлы проекта в рабочую директорию контейнера
COPY requirements.txt requirements.txt
COPY .. .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Запускаем приложение при старте контейнера
CMD ["python", "web/app.py"]