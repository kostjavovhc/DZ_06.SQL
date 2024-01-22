SELECT s.fullname, r.rate, sb.name, g.name, MAX(r.date_of) as last_date 
FROM students s JOIN rates r ON s.id = r.student_id
JOIN subjects sb ON r.subject_id = sb.id 
JOIN [groups] g ON g.id = s.group_id 
WHERE g.id  = 1 and sb.id  = 1
GROUP BY s.fullname, sb.name, r.rate, g.name 
ORDER BY last_date DESC
LIMIT 2;