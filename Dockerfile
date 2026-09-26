FROM gcc:13-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends cmake ninja-build python3 clang-format \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /makeling
COPY . .

CMD ["./makeling", "list"]
