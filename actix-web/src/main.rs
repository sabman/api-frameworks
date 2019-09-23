use actix_web::{web, App, HttpServer, Result};
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
    sample_value: String,
}

/// extract `Info` using serde
fn index(info: web::Json<Info>) -> Result<String> {
    return Ok(format!("Welcome {}!", info.sample_value))
}

fn main() {
    HttpServer::new(|| App::new().route("/", web::post().to(index)))
        .bind("127.0.0.1:8000")
        .unwrap()
        .run()
        .unwrap();
}