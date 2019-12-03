CREATE SCHEMA ticket;
USE ticket;


CREATE TABLE ticket (
  ticketnumber VARCHAR(255) NOT NULL,
  seatnumber VARCHAR(255) NOT NULL,
  flight_flight_number VARCHAR(255) NOT NULL,
  CONSTRAINT pkticketnumber PRIMARY KEY (ticketnumber)
);

USE ticket;
-- Insert ticket
INSERT INTO ticket (ticketnumber, seatnumber, flight_flight_number) 
VALUES ('0017645', '37B', 'CD 0073');
INSERT INTO ticket (ticketnumber, seatnumber, flight_flight_number) 
VALUES ('09876334', '47B', 'CD 3234');
INSERT INTO ticket (ticketnumber, seatnumber, flight_flight_number) 
VALUES ('54637826', '73X', 'CD 1223');
INSERT INTO ticket (ticketnumber, seatnumber, flight_flight_number) 
VALUES ('68527346', '87K', 'CD 0242');
INSERT INTO ticket (ticketnumber, seatnumber, flight_flight_number) 
VALUES ('00176453', '37B', 'CD 2524');