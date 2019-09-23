# api-frameworks

## Run actix-web

1. Make .env file and provide DATABASE_URL

2. Run migrations </br>
   `diesel migrations run`

3. Run Actix-Web </br>
   `cargo run`

### Calculate POST request time

curl -o /dev/null -s -w 'Total: %{time_total}s\n' http://127.0.0.1:8080/add/str
