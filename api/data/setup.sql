PRAGMA foreign_keys = ON;

-- can use VARCHAR(50) but SQLite doesn't encore this, so a trigger is required

BEGIN;

CREATE TABLE IF NOT EXISTS users
(
    id          INTEGER PRIMARY KEY,
    name        TEXT    NOT NULL,
    email       TEXT    NOT NULL UNIQUE,
    wallet_uuid TEXT    NOT NULL UNIQUE, -- blockchain wallet example 1Lbcfr7sAHTD9CgdQo3HTMTkV8LK4ZnX71
    deleted     INTEGER NULL             -- if deleted then set to 1 else NULL
);


CREATE TABLE IF NOT EXISTS transactions
(
    id                   INTEGER PRIMARY KEY,
    timestamp            INTEGER NOT NULL,
    cost                 INTEGER NOT NULL,
    sellers_wallet_uuid  TEXT    NOT NULL,
    customer_wallet_uuid TEXT    NOT NULL,
    product_uuid         INTEGER NOT NULL,
    delivery_option      TEXT    NOT NULL,
    longitude            REAL    NULL,
    latitude             REAL    NULL
);

CREATE TABLE IF NOT EXISTS products
(
    id           INTEGER PRIMARY KEY,
    cost         INTEGER NOT NULL,
    sellers_uuid TEXT    NOT NULL,
    description  TEXT    NOT NULL,
    title        TEXT    NOT NULL,
    deleted      INTEGER NULL,
    image_src    TEXT    NULL, --base64 image of product
    FOREIGN KEY (sellers_uuid) REFERENCES users (id) ON DELETE CASCADE
);


COMMIT;