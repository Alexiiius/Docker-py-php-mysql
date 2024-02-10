FROM python:3.8-slim-buster
WORKDIR /usr/src/app
ADD . /usr/src/app
RUN pip install flask
RUN pip install mysql-connector-python
EXPOSE 80
CMD ["python", "app.py"]