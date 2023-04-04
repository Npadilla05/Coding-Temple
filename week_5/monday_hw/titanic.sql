Count number of rows in data        
SELECT
COUNT(*)
FROM titanic

Total of people who survived
SELECT SUM("Survived")
FROM titanic

Passenger class with largest population
SELECT COUNT("Pclass") as passenger_class_count
FROM titanic
GROUP BY "Pclass"
ORDER BY "Pclass" asc  -> 3rd class has largest with 487