FROM python:3.9

WORKDIR /

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
