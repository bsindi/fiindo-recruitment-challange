FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .

# SSL-Workaround & pip update
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

COPY . .
CMD ["python", "src/main.py"]