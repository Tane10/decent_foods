use actix_web::HttpResponse;
use rusqlite::{Connection, params, Result};

pub fn main() -> Result<()> {

    let conn = Connection::open("data/dev_database.db")?;

    // let conn = match Connection::open("my_database.db") {
    //     Ok(conn) => conn,
    //     Err(e) => {
    //         eprintln!("Error opening database: {}", e);
    //         return HttpResponse::InternalServerError().finish();
    //     }
    // };




    conn.execute(
        "CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )",
        [],
    )?;

    conn.execute(
        "INSERT INTO user (name, email) VALUES (?1, ?2)",
        params!["Alice", "alice@example.com"],
    )?;

    let mut stmt = conn.prepare("SELECT id, name, email FROM user")?;
    let user_iter = stmt.query_map([], |row| {
        Ok(User {
            id: row.get(0)?,
            name: row.get(1)?,
            email: row.get(2)?,
        })
    })?;

    for user in user_iter {
        println!("Found user {:?}", user?);
    }

    Ok(())

}

#[derive(Debug)]
struct User {
    id: i32,
    name: String,
    email: String,
}
