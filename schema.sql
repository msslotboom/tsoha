CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE time (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    hours INTEGER,
    task INTEGER,
    logged_at TIMESTAMP
)