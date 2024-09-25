FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY ./Data .

WORKDIR /usr/src/app/Techniques

RUN make

WORKDIR /usr/src/app

RUN chmod -R +x measure.sh

CMD ["sh", "measure.sh"]
