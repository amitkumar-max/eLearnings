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
-- WITH cte AS (
--     SELECT id, title, ROW_NUMBER() OVER () AS rn
--     FROM courses_course
-- )
-- UPDATE courses_course
-- SET slug = lower(regexp_replace(cte.title, '\s+', '-', 'g')) || '-' || cte.rn
-- FROM cte
-- WHERE courses_course.id = cte.id;


-- SELECT * FROM courses_course;
-- SELECT column_name FROM information_schema.columns 
-- WHERE table_name='courses_course';

-- Agar slug column already exist nahi karta

-- Agar slug empty hai, temporary unique slug assign karo
-- UPDATE courses_course
-- SET slug = CONCAT(title, '-', id)
-- WHERE slug IS NULL OR slug = '';

-- TRUNCATE TABLE django_migrations;
-- DROP DATABASE IF EXISTS elearning_db_uk14;
-- CREATE DATABASE elearning_db_uk14;


-- Add the missing column back
-- ALTER TABLE django_content_type ADD COLUMN name varchar(100) NOT NULL DEFAULT '';
-- ALTER TABLE django_content_type ADD COLUMN name varchar(100) NOT NULL DEFAULT '';



-- ALTER TABLE courses_course
-- ADD COLUMN slug VARCHAR(255) UNIQUE;

-- ALTER TABLE courses_course
-- ADD COLUMN is_published BOOLEAN DEFAULT TRUE;

-- ALTER TABLE courses_course
-- ADD COLUMN slug VARCHAR(255) UNIQUE;



-- SELECT * FROM exams_course;
-- SELECT * FROM exams_exam;
SELECT * FROM courses_course;


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

