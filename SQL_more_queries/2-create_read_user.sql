-- Create the database 'hbtn_0d_2' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user 'user_0d_2' with a password, if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Revoke all privileges for this user on all databases to avoid undesired privileges
REVOKE ALL PRIVILEGES ON *.* FROM 'user_0d_2'@'localhost';

-- Revoke grant privileges to ensure they cannot grant privileges
REVOKE GRANT OPTION ON *.* FROM 'user_0d_2'@'localhost';

-- Only grant the SELECT privilege to 'user_0d_2' on the 'hbtn_0d_2' database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Immediately apply privilege changes
FLUSH PRIVILEGES;