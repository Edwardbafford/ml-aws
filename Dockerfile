FROM python:3.6-slim

WORKDIR /ml-aws

COPY . /ml-aws

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN python3 ./ml_aws/manage.py migrate

EXPOSE 80

CMD ["python3","./ml_aws/manage.py","runserver","0.0.0.0:80"]
