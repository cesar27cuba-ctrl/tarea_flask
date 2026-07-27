DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dni TEXT NOT NULL UNIQUE,
    given_name TEXT NOT NULL,
    family_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone_number TEXT,
    direccion TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (dni, given_name, family_name, email, phone_number, direccion) VALUES ('12345678', 'Juan', 'Pérez', 'juan@example.com', '+56912345678', 'Calle 1.');

INSERT INTO users (dni, given_name, family_name, email, phone_number, direccion) VALUES ('87654321', 'María', 'García', 'maria@example.com', '+56987654321', 'Calle 2.');

.headers on
.mode column