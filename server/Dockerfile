FROM python:3.7

RUN mkdir /server
WORKDIR /server
ADD . /server/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/server/server.py"]