-- Create a new table named 'force_name' if it does not already exist
CREATE TABLE IF NOT EXISTS force_name (
    -- 'id' column of type INT
    id INT,
    -- 'name' column of type VARCHAR(256) which cannot be NULL
    name VARCHAR(256) NOT NULL
);