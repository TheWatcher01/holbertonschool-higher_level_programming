-- Select the database
USE `hbtn_0c_0`;

-- Alters the database 'hbtn_0c_0' to use the 'utf8mb4' character set and 'utf8mb4_unicode_ci' collation
ALTER DATABASE `hbtn_0c_0` CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Alters the table 'first_table' to use the 'utf8mb4' character set and 'utf8mb4_unicode_ci' collation
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Alters the 'name' column in 'first_table' to use the 'utf8mb4' character set and 'utf8mb4_unicode_ci' collation
ALTER TABLE `first_table` CHANGE `name` `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
