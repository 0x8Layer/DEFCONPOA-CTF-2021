FROM python:3.7-alpine

WORKDIR /opt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001

RUN apk add --no-cache gcc musl-dev linux-headers python3-dev

COPY . .

RUN mv flag.txt /

RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["flask", "run"]

