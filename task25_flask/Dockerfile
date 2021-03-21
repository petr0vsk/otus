FROM python:3.8-buster

# для запуска контенейнера используйте: docker run -p 5000:5000 homework25
WORKDIR /var/app

COPY my_app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY my_app .

EXPOSE 5000
