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


-- ALTER TABLE courses_course
-- ADD COLUMN category VARCHAR(100),
-- ADD COLUMN price NUMERIC(10,2),
-- ADD COLUMN duration VARCHAR(50),
-- ADD COLUMN level VARCHAR(50);

INSERT INTO courses_course
(title, description, category, price, duration, level, image, teacher_id, is_published, slug, created_at, updated_at) VALUES

-- Programming
('Java Programming', 'Learn core Java concepts and OOP fundamentals.', 'Programming', 699.00, '5 weeks', 'Beginner', NULL, 1, TRUE, 'java-programming', NOW(), NOW()),
('Python for Data Science', 'Python programming for data analysis and ML.', 'Programming', 899.00, '6 weeks', 'Intermediate', NULL, 2, TRUE, 'python-data-science', NOW(), NOW()),
('C++ Fundamentals', 'Object-oriented programming with C++.', 'Programming', 799.00, '5 weeks', 'Beginner', NULL, 1, TRUE, 'cplusplus-fundamentals', NOW(), NOW()),
('JavaScript Essentials', 'Frontend scripting with JS.', 'Programming', 599.00, '4 weeks', 'Beginner', NULL, 2, TRUE, 'javascript-essentials', NOW(), NOW()),
('AI Programming with Python', 'Intro to AI and Machine Learning with Python.', 'Programming', 1199.00, '8 weeks', 'Advanced', NULL, 3, TRUE, 'ai-programming-python', NOW(), NOW()),

-- Design
('HTML & CSS Basics', 'Build static websites using HTML & CSS.', 'Design', 399.00, '3 weeks', 'Beginner', NULL, 1, TRUE, 'html-css-basics', NOW(), NOW()),
('JavaScript for Frontend', 'Interactive frontend development.', 'Design', 699.00, '5 weeks', 'Intermediate', NULL, 2, TRUE, 'javascript-frontend', NOW(), NOW()),
('Figma & UI Design', 'UI/UX design fundamentals using Figma.', 'Design', 499.00, '4 weeks', 'Beginner', NULL, 1, TRUE, 'figma-ui-design', NOW(), NOW()),
('Photoshop Basics', 'Image editing and design using Photoshop.', 'Design', 499.00, '4 weeks', 'Beginner', NULL, 2, TRUE, 'photoshop-basics', NOW(), NOW()),
('Corel Draw Essentials', 'Vector design using Corel Draw.', 'Design', 499.00, '3 weeks', 'Beginner', NULL, 1, TRUE, 'corel-draw-essentials', NOW(), NOW()),

-- Business
('Marketing 101', 'Introduction to marketing concepts.', 'Business', 599.00, '4 weeks', 'Beginner', NULL, 3, TRUE, 'marketing-101', NOW(), NOW()),
('Finance for Entrepreneurs', 'Basic finance principles for startups.', 'Business', 699.00, '5 weeks', 'Intermediate', NULL, 3, TRUE, 'finance-entrepreneurs', NOW(), NOW()),
('Accounting Basics', 'Understand accounting fundamentals.', 'Business', 599.00, '4 weeks', 'Beginner', NULL, 2, TRUE, 'accounting-basics', NOW(), NOW()),
('Business Strategy', 'Advanced business planning and strategy.', 'Business', 999.00, '6 weeks', 'Advanced', NULL, 1, TRUE, 'business-strategy', NOW(), NOW()),

-- Science
('Physics Fundamentals', 'Mechanics, optics, and thermodynamics.', 'Science', 699.00, '6 weeks', 'Beginner', NULL, 2, TRUE, 'physics-fundamentals', NOW(), NOW()),
('Chemistry Basics', 'Organic and inorganic chemistry introduction.', 'Science', 699.00, '6 weeks', 'Beginner', NULL, 2, TRUE, 'chemistry-basics', NOW(), NOW()),
('Biology Essentials', 'Cell biology, genetics, and ecology.', 'Science', 699.00, '5 weeks', 'Beginner', NULL, 3, TRUE, 'biology-essentials', NOW(), NOW()),

-- Mathematics
('Algebra Basics', 'Linear equations, polynomials, and functions.', 'Mathematics', 499.00, '4 weeks', 'Beginner', NULL, 1, TRUE, 'algebra-basics', NOW(), NOW()),
('Calculus Fundamentals', 'Limits, derivatives, and integrals.', 'Mathematics', 699.00, '5 weeks', 'Intermediate', NULL, 2, TRUE, 'calculus-fundamentals', NOW(), NOW()),
('Statistics for Beginners', 'Probability, data analysis, and stats concepts.', 'Mathematics', 599.00, '4 weeks', 'Beginner', NULL, 1, TRUE, 'statistics-beginners', NOW(), NOW()),
('Geometry Essentials', 'Triangles, circles, and 3D geometry basics.', 'Mathematics', 499.00, '4 weeks', 'Beginner', NULL, 2, TRUE, 'geometry-essentials', NOW(), NOW()),

-- Languages
('English Grammar', 'English grammar and writing skills.', 'Languages', 499.00, '3 weeks', 'Beginner', NULL, 3, TRUE, 'english-grammar', NOW(), NOW()),
('Hindi Language Basics', 'Learn Hindi reading, writing, and speaking.', 'Languages', 399.00, '3 weeks', 'Beginner', NULL, 1, TRUE, 'hindi-language-basics', NOW(), NOW()),
('Sanskrit Basics', 'Intro to Sanskrit language and grammar.', 'Languages', 499.00, '4 weeks', 'Beginner', NULL, 2, TRUE, 'sanskrit-basics', NOW(), NOW()),
('Spanish for Beginners', 'Learn basic Spanish conversation and grammar.', 'Languages', 599.00, '5 weeks', 'Beginner', NULL, 3, TRUE, 'spanish-beginners', NOW(), NOW()),

-- AI / Advanced Tech
('Prompt Engineering Basics', 'Learn how to craft prompts for AI systems.', 'Programming', 799.00, '4 weeks', 'Intermediate', NULL, 3, TRUE, 'prompt-engineering-basics', NOW(), NOW()),
('Machine Learning Fundamentals', 'Supervised & unsupervised ML concepts.', 'Programming', 1199.00, '8 weeks', 'Advanced', NULL, 3, TRUE, 'machine-learning-fundamentals', NOW(), NOW());



-- SELECT * FROM teachers;



-- -- 1️⃣ Create teachers table
-- CREATE TABLE teachers (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     email VARCHAR(255) UNIQUE NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );
c
-- -- 2️⃣ Insert 10 dummy teachers
-- INSERT INTO teachers (name, email) VALUES
-- ('John Doe', 'john@example.com'),
-- ('Jane Smith', 'jane@example.com'),
-- ('Alex Johnson', 'alex@example.com'),
-- ('Maria Garcia', 'maria@example.com'),
-- ('David Brown', 'david@example.com'),
-- ('Emily Davis', 'emily@example.com'),
-- ('Michael Wilson', 'michael@example.com'),
-- ('Sophia Martinez', 'sophia@example.com'),
-- ('Daniel Anderson', 'daniel@example.com'),
-- ('Olivia Thomas', 'olivia@example.com');









-- ALTER TABLE courses_course
-- ADD COLUMN image varchar(100);  -- ya jo type ImageField ka mapping hai (varchar/text for path)


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
-- SELECT * FROM courses_course;


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

