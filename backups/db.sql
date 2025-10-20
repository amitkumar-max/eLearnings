-- SELECT * FROM courses_course;
-- INSERT INTO courses_course (title, description, is_published, created_at, updated_at)
-- VALUES
-- ('HTML Fundamentals', 'Learn the structure of web pages using HTML5, semantic elements, and accessibility best practices.', TRUE, NOW(), NOW()),
-- ('CSS Mastery', 'Explore modern CSS3 with Flexbox, Grid, and animations to design responsive web layouts.', TRUE, NOW(), NOW()),
-- ('JavaScript Essentials', 'Understand the core of JavaScript — variables, functions, DOM, and ES6 features.', TRUE, NOW(), NOW()),
-- ('Java Programming Basics', 'Build a solid foundation in Java syntax, OOP, and data structures.', TRUE, NOW(), NOW()),
-- ('PHP with MySQL Integration', 'Create dynamic web apps and databases using PHP and MySQL together.', TRUE, NOW(), NOW()),
-- ('jQuery in Action', 'Simplify DOM manipulation, AJAX calls, and animations using the jQuery library.', TRUE, NOW(), NOW()),
-- ('MySQL Database Design', 'Master relational database design, joins, queries, and normalization.', TRUE, NOW(), NOW()),
-- ('Python for Developers', 'Learn Python programming for web, automation, and data applications.', TRUE, NOW(), NOW()),
-- ('C++ Programming Advanced', 'Understand OOP concepts, STL, and performance optimization using C++.', TRUE, NOW(), NOW()),
-- ('Django Full-Stack Development', 'Create robust web apps using Django ORM, templates, and REST framework.', TRUE, NOW(), NOW()),
-- ('ReactJS for Frontend Developers', 'Learn to build modern SPAs using ReactJS, hooks, and component architecture.', TRUE, NOW(), NOW()),
-- ('Bootstrap 5 Design System', 'Design responsive and mobile-first UI using the latest Bootstrap 5 framework.', TRUE, NOW(), NOW()),
-- ('NodeJS Backend Development', 'Create scalable backend systems using NodeJS, Express, and REST APIs.', TRUE, NOW(), NOW());

-- INSERT INTO lessons_lesson
-- (course_id, title, slug, content_text, content_path, order_index, created_at, updated_at)
-- VALUES
-- (1, 'HTML - Intro', 'html-intro', 'Content from intro.txt goes here...', 'lesson/content/html/intro.txt', 1, NOW(), NOW()),
-- (1, 'HTML - Content', 'html-content', 'Content from content.txt goes here...', 'lesson/content/html/content.txt', 2, NOW(), NOW()),
-- (1, 'HTML - Examples', 'html-examples', 'Content from examples.txt goes here...', 'lesson/content/html/examples.txt', 3, NOW(), NOW());

SELECT * FROM lessons_lesson WHERE course_id = 1;
