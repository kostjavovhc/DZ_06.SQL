SELECT sb.name, ROUND(AVG(r.rate), 2) as ave_rate
FROM rates r
JOIN subjects sb ON sb.id = r.subject_id 
JOIN teachers t ON t.id = sb.teacher_id 
WHERE t.id = 4
Group BY sb.name
ORDER BY ave_rate DESC;