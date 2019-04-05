FROM python:3.3
MAINTAINER Michael Pope "michaelpopedeveloper@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python", "app.py"]