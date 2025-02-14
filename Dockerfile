FROM python:3.10-slim

# Установка зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

# Экспорт портов и переменных окружения
ENV LOG_LEVEL=INFO
EXPOSE 8443

# Запуск приложения
CMD ["python", "-u", "bot.py"]