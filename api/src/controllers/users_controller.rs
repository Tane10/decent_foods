use crate::models::types::User;

pub async fn get_users() -> Vec<User> {
    user_service::fetch_users().await
}