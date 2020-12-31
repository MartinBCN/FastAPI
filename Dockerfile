FROM python:3.8

ENV DATA_DIR=/data
ENV MODEL_DIR=/models

COPY requirements.txt .

RUN pip install -r /requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
