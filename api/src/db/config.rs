use std::fs;
use rusqlite::{Connection, params, Result};


const DATABASE: Connection = Connection::open("data/dev_database.db")?;

fn setup() -> Result<()> {
    let sql_script = fs::read_to_string("data/setup.sql")
        .expect("Unable to read the SQL script file");

    DATABASE.execute_batch(&sql_script)?;
    Ok(())
}


pub fn main() -> Result<()> {
    setup()?;


    let mut stmt = DATABASE.prepare("SELECT id, name, email FROM user")?;
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
