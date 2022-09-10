FROM python:3.10
WORKDIR /code
COPY ipv4.py .
CMD [ "python", "./ipv4.py" ]