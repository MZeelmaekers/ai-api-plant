FROM ubuntu:20.04
WORKDIR /

RUN apt-get update --assume-yes
RUN apt-get install python --assume-yes
RUN apt install python3-pip

COPY ./api/requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install torch==1.7.0 -f https://download.pytorch.org/whl/torch_stable.html
RUN python -m pip install -r requirements.txt

COPY ./api .

EXPOSE 80

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
