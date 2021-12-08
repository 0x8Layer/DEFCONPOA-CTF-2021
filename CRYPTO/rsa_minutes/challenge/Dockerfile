FROM python:3.7-alpine

WORKDIR /opt

RUN apk add --no-cache gcc musl-dev linux-headers socat python3-dev

COPY . .
RUN pip install -r requirements.txt

EXPOSE 6000

CMD ["./start.sh"]

