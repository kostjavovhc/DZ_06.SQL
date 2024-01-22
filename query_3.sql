SELECT sb.name, g.name , ROUND(AVG(r.rate),2) as ave_rate
FROM rates r
JOIN students s ON r.student_id = s.id
JOIN [groups] g ON s.group_id = g.id 
JOIN subjects sb ON r.subject_id = sb.id 
WHERE sb.id = (?)
GROUP BY sb.name, g.name 
ORDER BY ave_rate DESC
;