-- Create a new table named 'id_not_null' if it does not already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    -- 'id' column of type INT with a default value of 1
    id INT DEFAULT 1,
    -- 'name' column of type VARCHAR(256)
    name VARCHAR(256)
);