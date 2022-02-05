FROM ubuntu:20.04

WORKDIR /app

RUN apt update
RUN apt install python3.9 -y && apt install pip -y

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/tests
CMD ["--url=http://192.168.0.103:8081/", "--admin_username=user", "--admin_password=bitnami"]
ENTRYPOINT ["pytest"]
