FROM python:3
MAINTAINER Keith Lia "keithlia@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD  [ "python", "./app.py" ]