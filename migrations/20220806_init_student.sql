CREATE TABLE IF NOT EXISTS students (
    id SERIAL UNIQUE NOT NULL,
    name VARCHAR ( 20 ) NOT NULL,
    address VARCHAR ( 50 ) NOT NULL,
    grade INT NOT NULL
);