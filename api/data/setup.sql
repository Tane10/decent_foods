CREATE TABLE IF NOT EXISTS users (
    uuid INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    wallet_uuid TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS transactions (
    uuid INTEGER PRIMARY KEY,
    timestamp INTEGER NOT NULL,
    cost INTEGER NOT NULL,
    sellers_wallet_uuid TEXT NOT NULL,
    customer_wallet_uuid TEXT NOT NULL,
    product_uuid INTEGER NOT NULL,
    delivery_option TEXT NOT NULL,
    longitude REAL,
    latitude REAL

)