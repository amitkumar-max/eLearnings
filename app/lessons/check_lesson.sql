-- -- SELECT * FROM lessons_lesson;



-- SELECT id, title, is_published
-- FROM courses_course
-- WHERE is_published = FALSE;


-- Verify slugs
-- SELECT id, title, slug FROM courses_course;


SELECT id, title, slug
FROM lessons_lesson
WHERE slug IS NULL OR slug = '';


-- UPDATE courses_course SET slug = 'full-stack-web-development' WHERE id = 2;
-- UPDATE courses_course SET slug = 'machine-learning-basics' WHERE id = 3;
-- UPDATE courses_course SET slug = 'data-structures-algorithms' WHERE id = 4;
-- UPDATE courses_course SET slug = 'intro-to-django' WHERE id = 5;



-- SELECT id, title, description
-- FROM courses_course
-- WHERE title = '' OR description = '' OR title IS NULL OR description IS NULL;


-- SELECT slug, COUNT(*) as total
-- FROM courses_course
-- GROUP BY slug
-- HAVING COUNT(*) > 1;




-- SELECT id, title, slug
-- FROM courses_course
-- WHERE slug IS NULL OR slug = '';


-- -- UPDATE courses_course 
-- -- SET slug = 'python-for-data-science'
-- -- WHERE id = 2;


-- -- -- Verify again
-- -- SELECT id, title, slug 
-- -- FROM courses_course 
-- -- WHERE id = 2;



-- SELECT * FROM courses_course;



-- SELECT id, title, slug, created_at
-- FROM courses_course
-- ORDER BY created_at DESC
-- LIMIT 5;
