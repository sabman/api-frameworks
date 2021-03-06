# api-frameworks

## Using Docker Compose

`docker-compose build`
`docker-compose up`

### Falcon-api migrations inside docker

`docker exec -it <container-id> alembic upgrade head`

## Run actix-web

1. Make .env file and provide DATABASE_URL

2. Run migrations </br>
   `diesel migration run`

3. Run Actix-Web </br>
   `cargo run`

## Run Falcon App

`gunicorn -b 0.0.0.0:7654 --reload falcon_api.app`

## Falcon migrations

`alembic upgrade head`

## Run falcon API tests

`python -m unittest tests/tests.py`

## Calculate POST request time

### For Actix-Web

`curl -s -o /dev/null -w "%{time_starttransfer}\n" -X POST http://127.0.0.1:8080/add/addnew -H 'cache-control: no-cache' -H 'postman-token: baf971b0-8e75-9113-0351-e144e35e6ae2'`

### For Falcon

`curl -s -o /dev/null -w "%{time_starttransfer}\n" -X POST 'http://0.0.0.0:7654/?name=addthistopostgres' -H 'cache-control: no-cache' -H 'content-type: application/x-www-form-urlencoded' -H 'postman-token: 826c277b-8d10-6384-e0fb-424f57189422' 0.049232`

# Heroku Falcon API

Push only subtree `falcon-api` to heroku master <br>

`git subtree push --prefix falcon-api heroku master`

# How to use Heroku Falcon API

API URL: `https://falcon-restful-api.herokuapp.com/api/v1/metrics`
request body type: `JSON(aplication/json)`
sample body: `{ "metric_value": 11111111111111111, "model_id": 5555555555555555 }`

Create User

- Request

```shell
curl -XPOST https://falcon-restful-api.herokuapp.com/api/v1/users -H "Content-Type: application/json" -d '{
 "email": "test1@gmail.com",
 "password": "test1234"
}'
```

- Response

```
returns 201 Status Code
```

Login User

- Request

```shell
curl -XGET https://falcon-restful-api.herokuapp.com/api/v1/user/sign_in -H "Content-Type: application/json" -d '{
 "email": "test.user@gmail.com",
 "password": "test1234"
}'
```

- Response

```json
{
  "token": "auth_token"
}
```

Post Metric Data

- Request

```shell
curl -X POST \
  https://falcon-restful-api.herokuapp.com/api/v1/metrics \
  -H 'authorization: auth_token' \
  -H 'content-type: application/json' \
  -d '{
 "value": 666,
 "model_ref": 666
}'
```

- Response

```
returns 201 Status Code
```
