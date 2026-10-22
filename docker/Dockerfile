ARG base_image=debian:12-slim
FROM $base_image
RUN apt update && apt install -y python3 python3-pip python3-venv
RUN python3 -m venv /build/py3 && \
    . /build/py3/bin/activate && \
    pip install --no-cache --upgrade pip setuptools wheel build twine pytest
WORKDIR /kaiib-api-wrapper-build
COPY requirements.txt ./
RUN . /build/py3/bin/activate && pip install --no-cache -U -r requirements.txt
COPY . .
ARG VERSION=26.0.0
RUN sed -i 's/^VERSION = "[^"]*"/VERSION = "'"$VERSION"'"/' setup.py
COPY .pypirc /root/.pypirc
RUN . /build/py3/bin/activate && \
    python3 -m pip install .