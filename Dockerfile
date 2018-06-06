FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update
RUN apt-get install -y --no-install-recommends nginx
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN apt-get install
ENTRYPOINT ["python"]
CMD ["application.py"]

EXPOSE 5000
 #CMD ["bash", "./production_run.sh"]