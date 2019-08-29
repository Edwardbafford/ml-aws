FROM python:3.6-slim

WORKDIR /ml-aws

COPY . /ml-aws

ARG public_key
ARG private_key

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN mkdir -p ./ml_aws/flowerapp/classifier/
RUN mkdir -p ./ml_aws/flowerapp/images/
RUN python3 ./download_classifier.py $public_key $private_key
RUN python3 ./ml_aws/manage.py migrate

EXPOSE 80

CMD ["python3","./ml_aws/manage.py","runserver","0.0.0.0:80"]
