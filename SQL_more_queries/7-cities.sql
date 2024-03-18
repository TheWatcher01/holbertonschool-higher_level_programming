-- Create the database 'hbtn_0d_usa' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switch to the 'hbtn_0d_usa' database for subsequent commands
USE hbtn_0d_usa;

-- Create the table 'cities' if it does not already exist
CREATE TABLE IF NOT EXISTS cities (
    -- 'id' column of type INT, which auto increments for each new record
    id INT AUTO_INCREMENT,
    -- 'state_id' column of type INT, which cannot be NULL
    state_id INT NOT NULL,
    -- 'name' column of type VARCHAR(256) which cannot be NULL
    name VARCHAR(256) NOT NULL,
    -- 'id' column is the primary key
    PRIMARY KEY (id),
    -- 'state_id' column is a foreign key that references the 'id' column in the 'states' table
    FOREIGN KEY (state_id) REFERENCES states(id)
) ENGINE=InnoDB;