SELECT sb.name, s.fullname, ROUND(AVG(r.rate),2) as ave_rate
FROM rates r
JOIN students s ON r.student_id = s.id
JOIN subjects sb ON r.subject_id = sb.id 
WHERE sb.id = 8
GROUP BY s.fullname 
ORDER BY ave_rate DESC 
LIMIT 1;