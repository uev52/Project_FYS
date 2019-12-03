CREATE SCHEMA ticket;
USE ticket;


CREATE TABLE ticket (
  ticketnumber VARCHAR(255) NOT NULL,
  seatnumber VARCHAR(255) NOT NULL,
  flight_flight_number VARCHAR(255) NOT NULL,
  PRIMARY KEY (ticketnumber),
  CONSTRAINT fk_Ticket_flight
    FOREIGN KEY (flight_number)
    REFERENCES flight (flight_number)
	,CONSTRAINT fk_Ticket_passengers
     FOREIGN KEY (passport_number)
    REFERENCES passengers (passport_number)
    
    
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