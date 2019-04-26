-- SQL INTRO - PROJECT

CREATE TABLE friends (
id INTEGER,
name TEXT,
birthday DATE
);

INSERT INTO friends (id, name, birthday) VALUES (1, 'Jane Doe', '1990-05-30');

-- Check for two things: Is friends table created? Is Jane Doe added to it?
-- SELECT * FROM friends;

INSERT INTO friends (id, name, birthday) VALUES (2, 'Anna Economou', '1999-12-06');

INSERT INTO friends (id, name, birthday) VALUES (3, 'Renos Lyssiotis', '1995-01-20');

UPDATE friends SET name = 'Jane Smith' WHERE id = 1;

-- SELECT * FROM friends;

ALTER TABLE friends ADD COLUMN email TEXT;

-- SELECT * FROM friends;

UPDATE friends SET email = 'jane@codecademy.com' WHERE id = 1;

UPDATE friends SET email = 'anna@codecademy.com' WHERE id = 2;

UPDATE friends SET email = 'renos@codecademy.com' WHERE id = 3;

-- SELECT * FROM friends;

-- DELETE FROM friends WHERE id = 1;

DELETE FROM friends WHERE name = 'Jane Smith';

SELECT * FROM friends;
