SELECT sb.name 
FROM rates r 
JOIN subjects sb ON r.subject_id = sb.id 
JOIN students s ON s.id = r.student_id 
WHERE s.id = 31
GROUP BY sb.name ;