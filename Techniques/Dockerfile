FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY ./Techniques ./Techniques

COPY ./RAPL ./RAPL

COPY ./measure.sh ./

WORKDIR /usr/src/app/Techniques

RUN make

WORKDIR /usr/src/app

CMD ["sh", "measure.sh"]
