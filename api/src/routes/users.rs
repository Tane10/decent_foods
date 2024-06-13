use actix_web::{HttpResponse, Responder, web};
use crate::controllers::users_controller;

pub fn config(cfg: &mut web::ServiceConfig) {
    cfg.service(
        web::scope("/users")
            .route("", web::get().to(get_users))
    );
}

async fn get_users() -> impl Responder {
    let users = users_controller::get_users().await;
    HttpResponse::Ok().json(users)
}