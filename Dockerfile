FROM python:3.8-slim

RUN mkdir src

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD jupyter notebook --ip=0.0.0.0 --no-browser --allow-root
