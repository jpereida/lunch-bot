USE LunchBot;

CREATE TABLE lunch_menu(
  lunch_date DATE NOT NULL,
  primary_meal varchar(700) NOT NULL,
  secondary_meal varchar(700) DEFAULT NULL
);

INSERT INTO lunch_menu(lunch_date, primary_meal, secondary_meal)
VALUES
("2017-08-15", "Spaghetti", NULL);