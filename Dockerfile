FROM amd64/python:3

WORKDIR /

COPY ./api/requirements.txt requirements.txt
RUN python
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./api .

EXPOSE 80

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
