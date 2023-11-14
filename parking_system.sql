CREATE DATABASE IF NOT EXISTS parking_system;

CREATE TABLE users(
name varchar(50),
username varchar(50),
password varchar(200),
role varchar(10),
userid varchar(20) primary key);

INSERT INTO users VALUES("admin", "admin", "$2b$12$rC3r6yhLAJFu8Ownd19wF.XSaPa5inXH2g0C3PXFtsHrEt.aqvw06", "admin", "A001");

CREATE TABLE employees(
fname varchar(50),
lname varchar(50),
empid varchar(50) primary key,
role varchar(10),
lot_no varchar(3),
address varchar(200));

CREATE TABLE vehicles(
reg_no varchar(10) primary key,
vehicle_type varchar(5),
driver_id varchar(20),
isparked tinyint(1) DEFAULT 0);

CREATE TABLE parked_vehicles(
reg_no varchar(10),
vehicle_type varchar(5),
entry_time DATETIME,
lot_no varchar(3),
CONSTRAINT FOREIGN KEY(reg_no) REFERENCES vehicles(reg_no));

CREATE TABLE cost_matrix(
vehicle_type varchar(5),
price int);

INSERT INTO cost_matrix(vehicle_type, price) VALUES("Car", 50), ("Bike", 0);

CREATE TABLE tickets(
reg_no varchar(10),
entry_time DATETIME,
exit_time DATETIME,
cost int);

DELIMITER //

CREATE TRIGGER after_parked_vehicle_insert
AFTER INSERT ON parked_vehicles
FOR EACH ROW
BEGIN
    UPDATE vehicles
    SET is_parked = 1
    WHERE reg_no = NEW.reg_no;
END;

//

CREATE TRIGGER after_parked_vehicle_delete
AFTER DELETE ON parked_vehicles
FOR EACH ROW
BEGIN
    UPDATE vehicles
    SET is_parked = 0
    WHERE reg_no = OLD.reg_no;
END;

//

DELIMITER ;
