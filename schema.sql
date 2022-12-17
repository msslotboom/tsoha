CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE forms (
    id SERIAL PRIMARY KEY,
    fields TEXT,
    title TEXT
);

CREATE TABLE time (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    hours INTEGER,
    task INTEGER,
    form INTEGER REFERENCES forms,
    logged_at TIMESTAMP
);

CREATE TABLE userform (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    form_id INTEGER REFERENCES forms,
    admin BOOLEAN
);