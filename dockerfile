FROM python

RUN apt-get update

# set work directory
WORKDIR /usr/src/app

COPY ./requirements.txt /code/requirements.txt
RUN pip install -U pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .