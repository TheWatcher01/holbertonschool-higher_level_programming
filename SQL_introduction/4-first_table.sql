-- Creates a table named 'first_table' if it does not exist, with 'id' as an integer column and 'name' as a variable character column of length 256
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);