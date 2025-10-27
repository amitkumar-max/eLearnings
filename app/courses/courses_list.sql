SELECT *
FROM courses_course
ORDER BY id ASC;


SELECT *
FROM lessons_lesson
ORDER BY course_id, id ASC;


-- SELECT 
--     l.id AS lesson_id,
--     l.title AS lesson_title,
--     l.slug AS lesson_slug,
--     c.title AS course_title,
--     c.slug AS course_slug
-- FROM lessons_lesson l
-- JOIN courses_course c ON l.course_id = c.id
-- ORDER BY c.id, l.id;



-- SELECT 
--     c.title AS course_title,
--     COUNT(l.id) AS total_lessons
-- FROM courses_course c
-- LEFT JOIN lessons_lesson l ON c.id = l.course_id
-- GROUP BY c.title
-- ORDER BY c.id;


SELECT l.title, l.slug, l.created_at
FROM lessons_lesson l
JOIN courses_course c ON l.course_id = c.id
WHERE c.title = 'Photoshop Basics'
ORDER BY l.id;

