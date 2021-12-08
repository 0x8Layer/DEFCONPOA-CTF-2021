FROM alpine:3.14

RUN apk add --no-cache gcc musl-dev linux-headers libc6-compat socat

WORKDIR /opt

COPY . .

EXPOSE 7000

CMD ["./start.sh"]
