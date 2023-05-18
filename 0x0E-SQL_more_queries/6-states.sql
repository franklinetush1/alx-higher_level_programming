-- Query to create database hbtn_0d_usa
CREATE DATABASE 
IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
       id INT UNIQUE AUTO_INCREMENT NOT NULL,
       PRIMARY KEY(id),
       name VARCHAR(256) NOT NULL);
