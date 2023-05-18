-- Create table id_not_null with unique id
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE NOT NULL PRIMARY KEY,
       name VARCHAR(256)
);
