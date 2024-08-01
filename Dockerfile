FROM python:3.10.3-slim

RUN mkdir web
WORKDIR /web

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python"]