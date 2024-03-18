-- Create a new table named 'unique_id' if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
    -- 'id' column of type INT with a default value of 1
    id INT DEFAULT 1,
    -- 'name' column of type VARCHAR(256)
    name VARCHAR(256),
    -- Ensure that the 'id' column values are unique
    UNIQUE (id)
);