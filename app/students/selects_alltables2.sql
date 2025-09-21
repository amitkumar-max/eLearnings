-- SELECT * FROM django_migrations;
-- SELECT * FROM auth_user;
-- SELECT * FROM auth_user_groups;
-- SELECT * FROM auth_group;
-- SELECT * FROM django_admin_log;
-- SELECT * FROM auth_group_permissions;
-- SELECT * FROM auth_user_user_permissions
-- SELECT * FROM django_admin_log;
-- SELECT * FROM django_content_type;
-- SELECT * FROM django_session;
-- Assign temporary unique slugs for all courses with empty slug
WITH cte AS (
    SELECT id, title, ROW_NUMBER() OVER () AS rn
    FROM courses_course
    WHERE slug = ''
)
UPDATE courses_course
SET slug = concat(slugify(title), '-', rn)
FROM cte
WHERE courses_course.id = cte.id;


-- SELECT * FROM exams_course;
-- SELECT * FROM exams_exam;


-- SELECT * FROM users_customuser;
-- check users table

-- SELECT table_name FROM information_schema.tables WHERE table_schema='public';

-- SELECT current_database(), current_user;


-- DROP SCHEMA public CASCADE;
-- CREATE SCHEMA public;

-- SELECT table_name FROM information_schema.tables 
-- WHERE table_schema='public';


-- SELECT * FROM users_customuser;

-- Correct table name
-- SELECT * FROM courses_course;
-- INSERT INTO courses_course (title, description, slug, is_published, created_at, updated_at)
-- VALUES 
-- ('Python Programming', 'Learn Python from scratch with hands-on projects.', 'python-programming', TRUE, NOW(), NOW()),
-- ('Web Development', 'HTML, CSS, JavaScript, Django full-stack course.', 'web-development', TRUE, NOW(), NOW()),
-- ('Data Science', 'Statistics, Python, and ML algorithms explained.', 'data-science', TRUE, NOW(), NOW());


-- SELECT * FROM app_courses;
-- SELECT id, title, slug, is_published FROM courses_course;







-- INSERT INTO exams_course (title, created_at, updated_at, is_published)
-- VALUES ('Dummy Course', NOW(), NOW(), TRUE)
-- RETURNING id;

-- INSERT INTO exams_exam 
-- (course_id, title, slug, exam_type, duration_minutes, total_marks, pass_percentage, created_at, updated_at, is_published) 
-- VALUES 
-- (1, 'Dummy Exam', 'dummy-exam', 'practice', 30, 100, 40.00, NOW(), NOW(), TRUE)
-- RETURNING id;

