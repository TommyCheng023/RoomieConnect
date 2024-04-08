CREATE DATABASE IF NOT EXISTS RoomieConnect;
USE RoomieConnect;

CREATE TABLE User (
    bu_email VARCHAR(100) PRIMARY KEY,
    password VARCHAR(100),
    self_description TEXT,
    roommate_expectation TEXT,
    name VARCHAR(100),
    gender VARCHAR(20),
    academic_classification VARCHAR(20),
    age TINYINT,
    building_preference1 VARCHAR(255),
    building_preference2 VARCHAR(255),
    building_preference3 VARCHAR(255),
    rent_budget INT
);