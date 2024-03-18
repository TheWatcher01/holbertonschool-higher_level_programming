-- Creates a table named 'second_table' if it does not exist, with 'id' as an integer column, 'name' as a variable character column of length 256, and 'score' as an integer column
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Inserts new records into 'second_table' with respective 'id', 'name', and 'score' values
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);