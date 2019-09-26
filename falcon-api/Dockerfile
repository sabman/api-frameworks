FROM python:3.7-alpine
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

COPY . .

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "--reload", "falcon-api.app"]
