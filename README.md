# api-frameworks

## Run actix-web

1. Make .env file and provide DATABASE_URL

2. Run migrations </br>
   `diesel migration run`

3. Run Actix-Web </br>
   `cargo run`

## Run Falcon App

`gunicorn -b 0.0.0.0:7654 --reload falcon-api.app`

## Calculate POST request time

### For Actix-Web

`curl -s -o /dev/null -w "%{time_starttransfer}\n" -X POST http://127.0.0.1:8080/add/addnew -H 'cache-control: no-cache' -H 'postman-token: baf971b0-8e75-9113-0351-e144e35e6ae2'`

### For Falcon

`curl -s -o /dev/null -w "%{time_starttransfer}\n" -X POST 'http://0.0.0.0:7654/?name=addthistopostgres' -H 'cache-control: no-cache' -H 'content-type: application/x-www-form-urlencoded' -H 'postman-token: 826c277b-8d10-6384-e0fb-424f57189422' 0.049232`
