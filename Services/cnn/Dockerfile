FROM python:3.6-slim

WORKDIR /cnn

COPY . /cnn

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python3","manage.py","runserver","0.0.0.0:80"]
