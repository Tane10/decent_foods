use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Clone)]
pub struct User {
    pub uuid: i32,
    pub name: String,
    pub email: String,
    pub wallet_uuid: String,
    delete: bool, // Rust maps to a single byte u8
}

//
// use crate::models::user::User;
// use std::sync::Mutex;
// use lazy_static::lazy_static;
//
// lazy_static! {
//     static ref USERS: Mutex<Vec<User>> = Mutex::new(Vec::new());
// }
//
// pub async fn fetch_users() -> Vec<User> {
//     let users = USERS.lock().unwrap();
//     users.clone()
// }
//
// pub async fn add_user(user: User) -> User {
//     let mut users = USERS.lock().unwrap();
//     users.push(user.clone());
//     user
// }