FROM python:3.9

WORKDIR /W2W_API

COPY .requirements.txt /W2W_API/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /W2W_API/requirements.txt

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "80"]