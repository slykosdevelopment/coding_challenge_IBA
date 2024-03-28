FROM python:3.6

COPY * /app/

WORKDIR /app

RUN pip install fastapi uvicorn

EXPOSE 8000

RUN chmod +x script_controller.sh

ENTRYPOINT ["./script_controller.sh"]