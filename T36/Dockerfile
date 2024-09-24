FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY ./src/T36/ .

RUN make

CMD ["./exec/break_sentence"]
