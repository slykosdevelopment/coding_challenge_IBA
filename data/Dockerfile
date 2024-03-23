FROM python:3.6

COPY main.py /app/

WORKDIR /app

RUN pip install fastapi

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
