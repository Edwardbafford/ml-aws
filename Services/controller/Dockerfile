FROM python:3.6-slim

WORKDIR /controller

COPY . /controller

RUN pwd
RUN ls
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN python3 manage.py migrate

EXPOSE 80

CMD ["python3","manage.py","runserver","0.0.0.0:80"]
