CREATE DATABASE IF NOT EXISTS parking_system;
USE parking_system;

CREATE TABLE users(
name varchar(50),
username varchar(50),
password varchar(200),
role varchar(10),
userid varchar(20) primary key);

INSERT INTO users VALUES("admin", "admin", "$2b$12$rC3r6yhLAJFu8Ownd19wF.XSaPa5inXH2g0C3PXFtsHrEt.aqvw06", "Admin", "A001");

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
    SET isparked = 1
    WHERE reg_no = NEW.reg_no;
END;

//

CREATE TRIGGER after_parked_vehicle_delete
AFTER DELETE ON parked_vehicles
FOR EACH ROW
BEGIN
    UPDATE vehicles
    SET isparked = 0
    WHERE reg_no = OLD.reg_no;
END;

//

DELIMITER ;


DELIMITER //

CREATE FUNCTION calculate_total_price(
    entry_time DATETIME,
    exit_time DATETIME,
    vehicle VARCHAR(5)
)
RETURNS DECIMAL(10, 2)
READS SQL DATA
BEGIN
    DECLARE duration_seconds INT;
    DECLARE duration_days DECIMAL(10, 2);
    DECLARE daily_price DECIMAL(10, 2);

    -- Calculate duration in seconds
    SET duration_seconds = TIMESTAMPDIFF(SECOND, entry_time, exit_time);

    -- Calculate duration in days
    SET duration_days = duration_seconds / (24 * 60 * 60);

    -- Retrieve the daily price from cost_matrix
    SELECT price INTO daily_price
    FROM parking_system.cost_matrix
    WHERE cost_matrix.vehicle_type = vehicle;

    -- Calculate total price
    RETURN duration_days * daily_price;
END //

DELIMITER ;

GRANT EXECUTE ON FUNCTION parking_system.calculate_total_price TO 'proj'@'localhost';