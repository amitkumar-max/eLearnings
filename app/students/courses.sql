-- -- Drop courses_course first because it depends on teachers
-- DROP TABLE IF EXISTS courses_course CASCADE;

-- CREATE TABLE courses_course (
--     id SERIAL PRIMARY KEY,
--     title VARCHAR(255) NOT NULL,
--     description TEXT,
--     category VARCHAR(100),
--     price NUMERIC(10,2),
--     duration VARCHAR(50),
--     level VARCHAR(50),
--     image VARCHAR(255),
--     teacher_id INT REFERENCES teachers(id),
--     is_published BOOLEAN DEFAULT FALSE,
--     slug VARCHAR(255),
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );



-- INSERT INTO courses_course
-- (title, description, category, price, duration, level, image, teacher_id, is_published, slug, created_at, updated_at) VALUES

-- -- Programming
-- ('Java Programming', 'Learn core Java concepts and OOP fundamentals.', 'Programming', 699.00, '5 weeks', 'Beginner', NULL, 1, TRUE, 'java-programming', NOW(), NOW()),
-- ('Python for Data Science', 'Python programming for data analysis and ML.', 'Programming', 899.00, '6 weeks', 'Intermediate', NULL, 2, TRUE, 'python-data-science', NOW(), NOW()),
-- ('C++ Fundamentals', 'Object-oriented programming with C++.', 'Programming', 799.00, '5 weeks', 'Beginner', NULL, 1, TRUE, 'cplusplus-fundamentals', NOW(), NOW()),
-- ('JavaScript Essentials', 'Frontend scripting with JS.', 'Programming', 599.00, '4 weeks', 'Beginner', NULL, 2, TRUE, 'javascript-essentials', NOW(), NOW()),
-- ('AI Programming with Python', 'Intro to AI and Machine Learning with Python.', 'Programming', 1199.00, '8 weeks', 'Advanced', NULL, 3, TRUE, 'ai-programming-python', NOW(), NOW()),

-- -- Design
-- ('HTML & CSS Basics', 'Build static websites using HTML & CSS.', 'Design', 399.00, '3 weeks', 'Beginner', NULL, 1, TRUE, 'html-css-basics', NOW(), NOW()),
-- ('JavaScript for Frontend', 'Interactive frontend development.', 'Design', 699.00, '5 weeks', 'Intermediate', NULL, 2, TRUE, 'javascript-frontend', NOW(), NOW()),
-- ('Figma & UI Design', 'UI/UX design fundamentals using Figma.', 'Design', 499.00, '4 weeks', 'Beginner', NULL, 1, TRUE, 'figma-ui-design', NOW(), NOW()),
-- ('Photoshop Basics', 'Image editing and design using Photoshop.', 'Design', 499.00, '4 weeks', 'Beginner', NULL, 2, TRUE, 'photoshop-basics', NOW(), NOW()),
-- ('Corel Draw Essentials', 'Vector design using Corel Draw.', 'Design', 499.00, '3 weeks', 'Beginner', NULL, 1, TRUE, 'corel-draw-essentials', NOW(), NOW()),

-- -- Business
-- ('Marketing 101', 'Introduction to marketing concepts.', 'Business', 599.00, '4 weeks', 'Beginner', NULL, 3, TRUE, 'marketing-101', NOW(), NOW()),
-- ('Finance for Entrepreneurs', 'Basic finance principles for startups.', 'Business', 699.00, '5 weeks', 'Intermediate', NULL, 3, TRUE, 'finance-entrepreneurs', NOW(), NOW()),
-- ('Accounting Basics', 'Understand accounting fundamentals.', 'Business', 599.00, '4 weeks', 'Beginner', NULL, 2, TRUE, 'accounting-basics', NOW(), NOW()),
-- ('Business Strategy', 'Advanced business planning and strategy.', 'Business', 999.00, '6 weeks', 'Advanced', NULL, 1, TRUE, 'business-strategy', NOW(), NOW()),

-- -- Science
-- ('Physics Fundamentals', 'Mechanics, optics, and thermodynamics.', 'Science', 699.00, '6 weeks', 'Beginner', NULL, 2, TRUE, 'physics-fundamentals', NOW(), NOW()),
-- ('Chemistry Basics', 'Organic and inorganic chemistry introduction.', 'Science', 699.00, '6 weeks', 'Beginner', NULL, 2, TRUE, 'chemistry-basics', NOW(), NOW()),
-- ('Biology Essentials', 'Cell biology, genetics, and ecology.', 'Science', 699.00, '5 weeks', 'Beginner', NULL, 3, TRUE, 'biology-essentials', NOW(), NOW()),

-- -- Mathematics
-- ('Algebra Basics', 'Linear equations, polynomials, and functions.', 'Mathematics', 499.00, '4 weeks', 'Beginner', NULL, 1, TRUE, 'algebra-basics', NOW(), NOW()),
-- ('Calculus Fundamentals', 'Limits, derivatives, and integrals.', 'Mathematics', 699.00, '5 weeks', 'Intermediate', NULL, 2, TRUE, 'calculus-fundamentals', NOW(), NOW()),
-- ('Statistics for Beginners', 'Probability, data analysis, and stats concepts.', 'Mathematics', 599.00, '4 weeks', 'Beginner', NULL, 1, TRUE, 'statistics-beginners', NOW(), NOW()),
-- ('Geometry Essentials', 'Triangles, circles, and 3D geometry basics.', 'Mathematics', 499.00, '4 weeks', 'Beginner', NULL, 2, TRUE, 'geometry-essentials', NOW(), NOW()),

-- -- Languages
-- ('English Grammar', 'English grammar and writing skills.', 'Languages', 499.00, '3 weeks', 'Beginner', NULL, 3, TRUE, 'english-grammar', NOW(), NOW()),
-- ('Hindi Language Basics', 'Learn Hindi reading, writing, and speaking.', 'Languages', 399.00, '3 weeks', 'Beginner', NULL, 1, TRUE, 'hindi-language-basics', NOW(), NOW()),
-- ('Sanskrit Basics', 'Intro to Sanskrit language and grammar.', 'Languages', 499.00, '4 weeks', 'Beginner', NULL, 2, TRUE, 'sanskrit-basics', NOW(), NOW()),
-- ('Spanish for Beginners', 'Learn basic Spanish conversation and grammar.', 'Languages', 599.00, '5 weeks', 'Beginner', NULL, 3, TRUE, 'spanish-beginners', NOW(), NOW()),

-- -- AI / Advanced Tech
-- ('Prompt Engineering Basics', 'Learn how to craft prompts for AI systems.', 'Programming', 799.00, '4 weeks', 'Intermediate', NULL, 3, TRUE, 'prompt-engineering-basics', NOW(), NOW()),
-- ('Machine Learning Fundamentals', 'Supervised & unsupervised ML concepts.', 'Programming', 1199.00, '8 weeks', 'Advanced', NULL, 3, TRUE, 'machine-learning-fundamentals', NOW(), NOW());



-- SELECT * FROM courses_course  ;

SELECT * FROM courses_lesson  ;
