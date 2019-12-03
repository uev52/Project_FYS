
USE passengers;

CREATE TABLE passengers (
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  passport_number VARCHAR(255) NOT NULL,
  country VARCHAR(255) NOT NULL,
  sex VARCHAR(255) NOT NULL,
  date_of_birth VARCHAR(255) NOT NULL,
  CONSTRAINT pkticketnumber PRIMARY KEY (ticketnumber)

);

USE passengers;
-- Insert passengers
INSERT INTO passengers (first_name, last_name, passport_number, country, sex, date_of_birth) 
VALUES ('Bart', 'Smit', 'speke3573', 'Netherlands', 'male', '6-1-1954');
INSERT INTO passengers (first_name, last_name, passport_number, country, sex, date_of_birth) 
VALUES ('Smith', 'hud', 'lohy7652', 'Netherlands', 'male', '16-12-1997');
INSERT INTO passengers (first_name, last_name, passport_number, country, sex, date_of_birth) 
VALUES ('Mohammed', 'Shaikh', 'julr4376', 'Egypt', 'male', '23-01-1984');
INSERT INTO passengers (first_name, last_name, passport_number, country, sex, date_of_birth) 
VALUES ('Maryam', 'Haidari', 'kjge2398', 'Iran', 'Female', '02-02-1996');
INSERT INTO passengers (first_name, last_name, passport_number, country, sex, date_of_birth) 
VALUES ('Ivo', 'Nijhuis', 'speke3573', 'Netherlands', 'male', '06-01-1954');
