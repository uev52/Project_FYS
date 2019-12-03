CREATE SCHEMA flight;
USE flight;

CREATE TABLE flight (
  flight_number VARCHAR(255) NOT NULL,
  aircraft VARCHAR(255) NOT NULL,
  origin VARCHAR(255) NOT NULL,
  destinantion VARCHAR(255) NOT NULL,
  flight_date VARCHAR(255) NOT NULL,
  CONSTRAINT pkflight_number PRIMARY KEY (flight_number)
);

USE flight;
-- Insert flight
INSERT INTO flight (flight_number, aircraft, origin, destinantion, flight_date) 
VALUES ('MNB312', 'A306', 'Schiphol', 'Ataturk', '01-12-2019');
INSERT INTO flight (flight_number, aircraft, origin, destinantion, flight_date)
VALUES ('CAI4V', 'B738', 'Schiphol', 'Antalya', '23-12-2019');
INSERT INTO flight (flight_number, aircraft, origin, destinantion, flight_date) 
VALUES ('ABC321', 'B753', 'Schiphol', 'Ibiza', '15-01-2020');
INSERT INTO flight (flight_number, aircraft, origin, destinantion, flight_date) 
VALUES ('OFG727', 'A311', 'Ibiza', 'Schiphol', '22-01-2020');
INSERT INTO flight (flight_number, aircraft, origin, destinantion, flight_date) 
VALUES ('PGM842', 'B737', 'Schiphol', 'Dpassengerubai', '07-04-2020');