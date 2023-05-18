-- Create table id_not_null with unique id
CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1 UNIQUE NOT NULL,
       name VARCHAR(256)
);
