-- Create the database 'hbtn_0d_usa' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switch to the 'hbtn_0d_usa' database for subsequent commands
USE hbtn_0d_usa;

-- Create the table 'states' if it does not already exist
CREATE TABLE IF NOT EXISTS states (
    -- 'id' column of type INT, which auto increments for each new record
    id INT AUTO_INCREMENT,
    -- 'name' column of type VARCHAR(256) which cannot be NULL
    name VARCHAR(256) NOT NULL,
    -- 'id' column is the primary key
    PRIMARY KEY (id)
) ENGINE=InnoDB;