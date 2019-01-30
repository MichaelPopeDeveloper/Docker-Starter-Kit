FROM python:3.3
MAINTAINER Michael Pope "michaelpopedeveloper@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]