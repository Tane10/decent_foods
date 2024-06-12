// mod users;
// mod food;

mod db;

use actix_web::{get, App, HttpResponse, HttpServer, Responder};

#[get("/")]
async fn index() -> impl Responder {
    let db_data = db::config::main();
    println!("{:?}", db_data);
    HttpResponse::Ok().body("hello world")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(index)
    })
        .bind("127.0.0.1:8080")?
        .run()
        .await
}