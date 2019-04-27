/*

Multiple Tables with REBU
Let’s practice what we learned about joins by combining rows from different tables.

Suppose you are a data analyst at REBU, a ridesharing platform. For a project, you were given three tables:

trips - trips information
riders - users data
cars - autonomous cars

*/

SELECT * FROM trips;

SELECT * FROM riders;

SELECT * FROM cars;

SELECT *
FROM riders
CROSS JOIN cars;

SELECT *
FROM trips
LEFT JOIN riders
ON trips.rider_id = riders.id;

SELECT *
FROM trips
JOIN cars
ON trips.car_id = cars.id;

SELECT *
FROM riders
UNION
SELECT *
FROM riders2;

SELECT AVG(cost) FROM trips;

SELECT *
FROM riders
WHERE total_trips < 500;

SELECT COUNT(*)
FROM cars
WHERE status = 'active';

SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;
