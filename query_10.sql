SELECT sb.name
FROM rates r 
JOIN subjects sb ON r.subject_id = sb.id 
JOIN students s ON s.id = r.student_id
JOIN teachers t ON t.id = sb.teacher_id
WHERE s.id = 27 and t.id = 1
GROUP BY sb.name ;