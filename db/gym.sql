DROP TABLE bookings;
DROP TABLE members;
DROP TABLE sessions;

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    upcoming BOOLEAN
);

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    session_id INT REFERENCES sessions(id) ON DELETE CASCADE
);