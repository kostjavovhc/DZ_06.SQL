SELECT s.fullname, ROUND(AVG(r.rate),2) as ave_rate
FROM rates r
JOIN students s ON r.student_id = s.id
GROUP BY s.fullname 
ORDER BY ave_rate DESC 
LIMIT 5;