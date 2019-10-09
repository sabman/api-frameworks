# Falcon REST API with PostgreSQL

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ziwon/falcon-rest-api)

Simple REST API using Falcon web framework.

Falcon is a high-performance Python framework for building cloud APIs, smart proxies, and app backends. More information can be found [here](https://github.com/falconry/falcon/).

# Requirements

This project uses [virtualenv](https://virtualenv.pypa.io/en/stable/) as isolated Python environment for installation and running. Therefore, [virtualenv](https://virtualenv.pypa.io/en/stable/) must be installed. And you may need a related dependency library for a PostgreSQL database. See [install.sh](https://github.com/ziwon/falcon-rest-api/blob/master/install.sh) for details.

# Run Server

`gunicorn -b 127.0.0.1:5000 --reload app.main:application`

# Deploy

You need to set `APP_ENV` environment variables before deployment. You can set LIVE mode in Linux/Heroku as follows.

## Linux

In Linux, just set `APP_ENV` to run in live mode.

```shell
export APP_ENV=live
```

## Heroku

In Heroku, use the command `config:set`. (See [here](https://devcenter.heroku.com/articles/config-vars) for details)

```shell
heroku config:set APP_ENV=live
```

# Usage

Create an user

- Request Localhost

```shell
curl -XPOST http://localhost:5000/api/v1/users -H "Content-Type: application/json" -d '{
 "email": "test1@gmail.com",
 "password": "test1234"
}'
```

- Request Production

```shell
curl -XPOST https://falcon-restful-api.herokuapp.com/api/v1/users -H "Content-Type: application/json" -d '{
 "email": "test1@gmail.com",
 "password": "test1234"
}'
```

- Response

```json
returns 201 Status Code
```

Log in with email and password

- Request Localhost

```shell
curl -XGET https://falcon-restful-api.herokuapp.com/api/v1/user/sign_in -H "Content-Type: application/json" -d '{
 "email": "test1@gmail.com",
 "password": "test1234"
}'
```

- Request Production

```shell
curl -XGET http://localhost:5000/api/v1/user/sign_in -H "Content-Type: application/json" -d '{
 "email": "test1@gmail.com",
 "password": "test1234"
}'
```

- Response

```json
{
  "token": "token_value"
}
```

Post Metric Data

- Request

```shell
curl -X POST \
  http://localhost:5000/api/v1/metrics \
  -H 'authorization: gAAAAABdnbuh48BlzYglrJYvzsYh_vpYM_rE5XWBC8SIo4L-lDVb_ujAGWpgOYWKUjojSAk8ZGGswP9YKWG8wwpUPDJcpzwLCw==' \
  -H 'content-type: application/json' \
  -d '{
 "value": 666,
 "model_ref": 666
}'
```

```shell
curl -X POST \
  https://falcon-restful-api.herokuapp.com/api/v1/metrics \
  -H 'authorization: gAAAAABdnbuh48BlzYglrJYvzsYh_vpYM_rE5XWBC8SIo4L-lDVb_ujAGWpgOYWKUjojSAk8ZGGswP9YKWG8wwpUPDJcpzwLCw==' \
  -H 'content-type: application/json' \
  -d '{
 "value": 666,
 "model_ref": 666
}'
```

Check the validation of requested data

- Request

```shell
curl -XPOST http://localhost:5000/api/v1/users -H "Content-Type: application/json" -d '{
 "email": "test1@gmail.c",
 "password": "123"
}'
```

- Response

```json
{
  "meta": {
    "code": 88,
    "message": "Invalid Parameter",
    "description": {
      "username": "min length is 4",
      "email": "value does not match regex '[a-zA-Z0-9._-]+@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,4}'",
      "password": [
        "value does not match regex '[0-9a-zA-Z]\\w{3,14}'",
        "min length is 8"
      ]
    }
  }
}
```

Get database rollback error in response for duplicated data

- Request

```shell
curl -XPOST http://localhost:5000/api/v1/users -H "Content-Type: application/json" -d '{
 "email": "test1@gmail.com",
 "password": "test1234"
}'
```

- Response

```json
{
  "meta": {
    "code": 77,
    "message": "Database Rollback Error",
    "description": {
      "details": "(psycopg2.IntegrityError) duplicate key value violates unique constraint \"user_email_key\"\nDETAIL:  Key (email)=(test1@gmail.com) already exists.\n",
      "params": "{'username': 'test1', 'token': 'gAAAAABV-UCq_DneJyz4DTuE6Fuw68JU7BN6fLdxHHIlu42R99sjWFFonrw3eZx7nr7ioIFSa7Akk1nWgGNmY3myJzqqbpOsJw==', 'sid': '6716985526', 'email': 'test1@gmail.com', 'password': '$2a$12$KNlGvL1CP..6VNjqQ0pcjukj/fC88sc1Zpzi0uphIUlG5MjyAp2fS'}"
    }
  }
}
```
