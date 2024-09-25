FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    g++ \
    make \
    kmod \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /package

RUN make

CMD ["sh", "measure.sh"]
