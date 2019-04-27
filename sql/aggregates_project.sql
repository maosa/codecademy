SELECT * FROM startups;

SELECT COUNT(*) FROM startups;

SELECT SUM(valuation) FROM startups;

SELECT MAX(raised) FROM startups;

SELECT MAX(raised)
FROM startups
WHERE stage = 'Seed';

SELECT name, MIN(founded)
FROM startups;

SELECT category, ROUND(AVG(valuation), 2)
FROM startups
GROUP BY 1
ORDER BY 2 DESC;

SELECT category, COUNT(name)
FROM startups
GROUP BY 1
HAVING COUNT(name) > 3;

SELECT name, ROUND(AVG(employees), 0)
FROM startups
GROUP BY location
HAVING AVG(employees) > 500;
