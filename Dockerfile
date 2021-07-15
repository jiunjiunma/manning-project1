FROM python:3.8-slim

RUN mkdir src

WORKDIR /src

COPY requirements.txt .

COPY main.py /src

COPY model.joblib /src

RUN pip install -r requirements.txt

#CMD jupyter notebook --ip=0.0.0.0 --no-browser --allow-root

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000 
