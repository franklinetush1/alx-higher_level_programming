-- Create table id_not_null with unique id
CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1 UNIQUE AUTO_INCREMENT,
       name VARCHAR(256)
);
