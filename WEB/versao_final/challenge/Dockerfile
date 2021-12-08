FROM python:3.7-alpine

WORKDIR /opt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5003

RUN apk add --no-cache gcc musl-dev linux-headers python3-dev

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5003

CMD ["flask", "run"]
