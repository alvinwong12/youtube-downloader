FROM python:3.7

RUN mkdir /server
WORKDIR /server
ADD . /server/
RUN pip install -r requirements.txt
RUN apt-get update -y
RUN apt-get install ffmpeg -y

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]