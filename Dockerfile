FROM python:3.9
WORKDIR /

COPY ./api/requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install torch==1.10.2 torchvision==0.11.3 -f https://download.pytorch.org/whl/torch_stable.html
RUN python -m pip install -r requirements.txt

COPY ./api .

EXPOSE 80

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
