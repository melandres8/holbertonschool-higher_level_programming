-- top 3 of cities temperature
SELECT city, MAX(value) as max_temp FROM temperatures GROUP BY city ORDER BY city DESC LIMIT 3;

