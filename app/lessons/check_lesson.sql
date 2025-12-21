-- SELECT * FROM lessons_lesson;
-- -- SELECT * FROM courses_course;
-- SELECT * FROM teachers_teacherprofile;
-- -- SELECT * FROM  users_customuser; 
-- \dt
-- \dt   -- saare tables
SELECT * FROM lessons_lesson;


-- -- -- ✅ Insert Dummy Tech Courses in courses_course Table
-- -- INSERT INTO courses_course
-- -- (id, created_at, updated_at, teacher_id, description, image, is_published, slug, title)
-- -- VALUES
-- -- (1, NOW(), NOW(), NULL, 'Learn the basics of JavaScript programming', 'javascript.png', TRUE, 'javascript', 'JavaScript'),

-- -- (2, NOW(), NOW(), NULL, 'Master jQuery and DOM manipulation for interactive web design', 'jquery.png', TRUE, 'jquery', 'jQuery'),

-- -- (3, NOW(), NOW(), NULL, 'Learn the fundamentals of C++ programming with examples', 'cpp.png', TRUE, 'c-plus-plus', 'C++'),

-- -- (4, NOW(), NOW(), NULL, 'Understand MySQL databases, queries, and relationships', 'mysql.png', TRUE, 'mysql', 'MySQL'),

-- -- (5, NOW(), NOW(), NULL, 'Learn Node.js and build scalable backend APIs', 'nodejs.png', TRUE, 'nodejs', 'Node.js'),

-- -- (6, NOW(), NOW(), NULL, 'Master ReactJS to create modern, dynamic web apps', 'reactjs.png', TRUE, 'reactjs', 'ReactJS'),

-- -- (7, NOW(), NOW(), NULL, 'Learn the structure of web pages using HTML5', 'html.png', TRUE, 'html', 'HTML'),

-- -- (8, NOW(), NOW(), NULL, 'Design beautiful web layouts using CSS3', 'css.png', TRUE, 'css', 'CSS'),

-- -- (9, NOW(), NOW(), NULL, 'Learn Bootstrap framework for responsive design', 'bootstrap.png', TRUE, 'bootstrap', 'Bootstrap'),

-- -- (10, NOW(), NOW(), NULL, 'Get started with Python — the most versatile programming language', 'python.png', TRUE, 'python', 'Python'),

-- -- (11, NOW(), NOW(), NULL, 'Learn Java from scratch — from OOP to advanced concepts', 'java.png', TRUE, 'java', 'Java'),

-- -- (12, NOW(), NOW(), NULL, 'Understand PHP and backend web development fundamentals', 'php.png', TRUE, 'php', 'PHP'),

-- -- (13, NOW(), NOW(), NULL, 'Build and deploy web apps using Django framework', 'django.png', TRUE, 'django', 'Django');


-- INSERT INTO courses_course
-- (created_at, updated_at, teacher_id, description, image, is_published, slug, title)
-- VALUES
-- (NOW(), NOW(), NULL, 'Learn the basics of JavaScript programming', 'javascript.png', TRUE, 'javascript', 'JavaScript'),
-- (NOW(), NOW(), NULL, 'Master jQuery and DOM manipulation for interactive web design', 'jquery.png', TRUE, 'jquery', 'jQuery'),
-- (NOW(), NOW(), NULL, 'Learn the fundamentals of C++ programming with examples', 'cpp.png', TRUE, 'c-plus-plus', 'C++'),
-- (NOW(), NOW(), NULL, 'Understand MySQL databases, queries, and relationships', 'mysql.png', TRUE, 'mysql', 'MySQL'),
-- (NOW(), NOW(), NULL, 'Learn Node.js and build scalable backend APIs', 'nodejs.png', TRUE, 'nodejs', 'Node.js'),
-- (NOW(), NOW(), NULL, 'Master ReactJS to create modern, dynamic web apps', 'reactjs.png', TRUE, 'reactjs', 'ReactJS'),
-- (NOW(), NOW(), NULL, 'Learn the structure of web pages using HTML5', 'html.png', TRUE, 'html', 'HTML'),
-- (NOW(), NOW(), NULL, 'Design beautiful web layouts using CSS3', 'css.png', TRUE, 'css', 'CSS'),
-- (NOW(), NOW(), NULL, 'Learn Bootstrap framework for responsive design', 'bootstrap.png', TRUE, 'bootstrap', 'Bootstrap'),
-- (NOW(), NOW(), NULL, 'Get started with Python — the most versatile programming language', 'python.png', TRUE, 'python', 'Python'),
-- (NOW(), NOW(), NULL, 'Learn Java from scratch — from OOP to advanced concepts', 'java.png', TRUE, 'java', 'Java'),
-- (NOW(), NOW(), NULL, 'Understand PHP and backend web development fundamentals', 'php.png', TRUE, 'php', 'PHP'),
-- (NOW(), NOW(), NULL, 'Build and deploy web apps using Django framework', 'django.png', TRUE, 'django', 'Django');




-- -- INSERT INTO teachers_teacherprofile 
-- -- (id, created_at, updated_at, bio, statistics, awards, profile_views, social_links, user_id)
-- -- VALUES
-- -- (1, NOW(), NOW(), 'Experienced Python developer and mentor.', '5 years teaching', 'Top Instructor Award 2023', 250, '{"linkedin": "https://linkedin.com/teacher1"}', 1),
-- -- (2, NOW(), NOW(), 'Full-stack web teacher specialized in Django and React.', '3 years teaching', 'Mentor of the Year 2024', 180, '{"github": "https://github.com/teacher2"}', 2),
-- -- (3, NOW(), NOW(), 'Machine learning enthusiast and Python expert.', '4 years teaching', 'AI Researcher Recognition', 220, '{"twitter": "https://twitter.com/teacher3"}', 3),
-- -- (4, NOW(), NOW(), 'Backend engineer with Node.js and SQL expertise.', '6 years teaching', 'Most Reliable Mentor', 300, '{"website": "https://teacher4.dev"}', 4),
-- -- (5, NOW(), NOW(), 'Creative web designer with UI/UX experience.', '2 years teaching', 'Design Excellence Award', 90, '{"dribbble": "https://dribbble.com/teacher5"}', 5);

-- -- INSERT INTO teachers_teacherprofile (id, full_name, email, created_at, updated_at)
-- -- VALUES
-- -- (1, 'Teacher One', 'teacher1@example.com', NOW(), NOW()),
-- -- (2, 'Teacher Two', 'teacher2@example.com', NOW(), NOW()),
-- -- (3, 'Teacher Three', 'teacher3@example.com', NOW(), NOW()),
-- -- (4, 'Teacher Four', 'teacher4@example.com', NOW(), NOW()),
-- -- (5, 'Teacher Five', 'teacher5@example.com', NOW(), NOW());



-- -- SELECT id, user_id, name FROM teachers_teacherprofile;


-- -- SELECT column_name, data_type, is_nullable, column_default
-- -- FROM information_schema.columns
-- -- WHERE table_schema = 'public'
-- --   AND table_name = 'teachers_teacherprofile'
-- -- ORDER BY ordinal_position;

-- -- SELECT column_name, data_type, is_nullable, column_default
-- -- FROM information_schema.columns
-- -- WHERE table_schema = 'public'
-- --   AND table_name = 'users_customuser'
-- -- ORDER BY ordinal_position;


-- -- INSERT INTO lessons_lesson (title, slug, order_index, course_id, created_at, updated_at, content_file)
-- -- VALUES
-- -- ('Accounting Basics', 'accounting-basics', 1, 1, NOW(), NOW(), 'accounting-basics.txt'),
-- -- ('AI Programming with Python', 'ai-programming-with-python', 1, 2, NOW(), NOW(), 'ai-programming-with-python.txt'),
-- -- ('Algebra Basics', 'algebra-basics', 1, 3, NOW(), NOW(), 'algebra-basics.txt'),
-- -- ('Biology Essentials', 'biology-essentials', 1, 4, NOW(), NOW(), 'biology-essentials.txt'),
-- -- ('English Grammar', 'english-grammar', 1, 5, NOW(), NOW(), 'english-grammar.txt'),
-- -- ('Geometry Essentials', 'geometry-essentials', 1, 6, NOW(), NOW(), 'geometry-essentials.txt'),
-- -- ('Java Programming', 'java-programming', 1, 7, NOW(), NOW(), 'java-programming.txt'),
-- -- ('Photoshop Basics', 'photoshop-basics', 1, 8, NOW(), NOW(), 'photoshop-basics.txt'),
-- -- ('Python for Data Science', 'python-for-data-science', 1, 9, NOW(), NOW(), 'python-for-data-science.txt');



-- -- INSERT INTO courses_course (created_at, updated_at, teacher_id, description, image, is_published, slug, title)
-- -- VALUES
-- -- (NOW(), NOW(), 1, 'Master accounting principles from scratch.', 'accounting.jpg', TRUE, 'accounting-basics', 'Accounting Basics'),
-- -- (NOW(), NOW(), 1, 'Learn AI programming using Python fundamentals.', 'ai-python.jpg', TRUE, 'ai-programming-with-python', 'AI Programming with Python'),
-- -- (NOW(), NOW(), 1, 'Understand the essentials of algebra.', 'algebra.jpg', TRUE, 'algebra-basics', 'Algebra Basics'),
-- -- (NOW(), NOW(), 1, 'Explore biology core concepts and essentials.', 'biology.jpg', TRUE, 'biology-essentials', 'Biology Essentials'),
-- -- (NOW(), NOW(), 1, 'Master the rules and structure of English Grammar.', 'english.jpg', TRUE, 'english-grammar', 'English Grammar'),
-- -- (NOW(), NOW(), 1, 'Build strong geometric visualization skills.', 'geometry.jpg', TRUE, 'geometry-essentials', 'Geometry Essentials'),
-- -- (NOW(), NOW(), 1, 'Dive deep into Java programming concepts.', 'java.jpg', TRUE, 'java-programming', 'Java Programming'),
-- -- (NOW(), NOW(), 1, 'Learn Photoshop tools and image editing basics.', 'photoshop.jpg', TRUE, 'photoshop-basics', 'Photoshop Basics'),
-- -- (NOW(), NOW(), 1, 'Explore Python techniques for data science and analytics.', 'python-data.jpg', TRUE, 'python-for-data-science', 'Python for Data Science');





-- -- INSERT INTO courses_course 
-- -- (id, created_at, updated_at, teacher_id, description, image, is_published, slug, title)
-- -- VALUES
-- -- (1, NOW(), NOW(), 101, 'Learn Python from scratch', 'python.png', 1, 'python-for-beginners', 'Python for Beginners'),
-- -- (2, NOW(), NOW(), 102, 'Master Django framework', 'django.png', 1, 'django-masterclass', 'Django Masterclass'),
-- -- (3, NOW(), NOW(), 103, 'JavaScript for web development', 'js.png', 1, 'js-web-dev', 'JavaScript Web Development'),
-- -- (4, NOW(), NOW(), 104, 'Data Science with Python', 'datasci.png', 0, 'data-science-python', 'Data Science with Python'),
-- -- (5, NOW(), NOW(), 105, 'Fullstack Development Bootcamp', 'fullstack.png', 1, 'fullstack-bootcamp', 'Fullstack Development Bootcamp');
-- -- 'teachers_teacherprofile',

-- -- SELECT * FROM teachers_teacherprofile;



-- -- Only if your FK allows nulls
-- -- INSERT INTO courses_course
-- -- (id, created_at, updated_at, teacher_id, description, image, is_published, slug, title)
-- -- VALUES
-- -- (1, NOW(), NOW(), NULL, 'Learn the basics of Accounting', 'accounting.png', TRUE, 'accounting-basics', 'Accounting Basics');


-- -- -- Corrected version for PostgreSQL
-- -- INSERT INTO courses_course
-- -- (id, created_at, updated_at, teacher_id, description, image, is_published, slug, title)
-- -- VALUES
-- -- (1, NOW(), NOW(), 1, 'Learn the basics of Accounting', 'accounting.png', TRUE, 'accounting-basics', 'Accounting Basics'),
-- -- (2, NOW(), NOW(), 1, 'AI programming with Python course', 'ai-python.png', TRUE, 'ai-programming-with-python', 'AI Programming with Python'),
-- -- (3, NOW(), NOW(), 1, 'Learn Algebra from scratch', 'algebra.png', TRUE, 'algebra-basics', 'Algebra Basics'),
-- -- (4, NOW(), NOW(), 1, 'Biology essentials for beginners', 'biology.png', TRUE, 'biology-essentials', 'Biology Essentials'),
-- -- (5, NOW(), NOW(), 1, 'English Grammar fundamentals', 'english.png', TRUE, 'english-grammar', 'English Grammar'),
-- -- (6, NOW(), NOW(), 1, 'Geometry essentials', 'geometry.png', TRUE, 'geometry-essentials', 'Geometry Essentials'),
-- -- (7, NOW(), NOW(), 1, 'Java programming course', 'java.png', TRUE, 'java-programming', 'Java Programming'),
-- -- (8, NOW(), NOW(), 1, 'Photoshop basics', 'photoshop.png', TRUE, 'photoshop-basics', 'Photoshop Basics'),
-- -- (9, NOW(), NOW(), 1, 'Python for Data Science', 'python-data.png', TRUE, 'python-for-data-science', 'Python for Data Science');

-- -- Insert courses
-- -- INSERT INTO courses_course
-- -- (id, created_at, updated_at, teacher_id, description, image, is_published, slug, title)
-- -- VALUES
-- -- (1, NOW(), NOW(), 1, 'Learn the basics of Accounting', 'accounting.png', 1, 'accounting-basics', 'Accounting Basics'),
-- -- (2, NOW(), NOW(), 1, 'AI programming with Python course', 'ai-python.png', 1, 'ai-programming-with-python', 'AI Programming with Python'),
-- -- (3, NOW(), NOW(), 1, 'Learn Algebra from scratch', 'algebra.png', 1, 'algebra-basics', 'Algebra Basics'),
-- -- (4, NOW(), NOW(), 1, 'Biology essentials for beginners', 'biology.png', 1, 'biology-essentials', 'Biology Essentials'),
-- -- (5, NOW(), NOW(), 1, 'English Grammar fundamentals', 'english.png', 1, 'english-grammar', 'English Grammar'),
-- -- (6, NOW(), NOW(), 1, 'Geometry essentials', 'geometry.png', 1, 'geometry-essentials', 'Geometry Essentials'),
-- -- (7, NOW(), NOW(), 1, 'Java programming course', 'java.png', 1, 'java-programming', 'Java Programming'),
-- -- (8, NOW(), NOW(), 1, 'Photoshop basics', 'photoshop.png', 1, 'photoshop-basics', 'Photoshop Basics'),
-- -- (9, NOW(), NOW(), 1, 'Python for Data Science', 'python-data.png', 1, 'python-for-data-science', 'Python for Data Science');


-- -- INSERT INTO lessons_lesson 
-- -- (id, title, slug, order_index, course_id, created_at, updated_at, content_file)
-- -- VALUES
-- -- (1, 'Introduction to Python', 'intro-python', 1, 1, NOW(), NOW(), 'lesson1.pdf'),
-- -- (2, 'Python Variables & Data Types', 'python-variables', 2, 1, NOW(), NOW(), 'lesson2.pdf'),
-- -- (3, 'Control Structures in Python', 'python-control', 3, 1, NOW(), NOW(), 'lesson3.pdf'),
-- -- (4, 'Django Setup & Installation', 'django-setup', 1, 2, NOW(), NOW(), 'lesson1.pdf'),
-- -- (5, 'Django Models & ORM', 'django-models', 2, 2, NOW(), NOW(), 'lesson2.pdf'),
-- -- (6, 'Django Views & Templates', 'django-views', 3, 2, NOW(), NOW(), 'lesson3.pdf'),
-- -- (7, 'JavaScript Basics', 'js-basics', 1, 3, NOW(), NOW(), 'lesson1.pdf'),
-- -- (8, 'DOM Manipulation', 'js-dom', 2, 3, NOW(), NOW(), 'lesson2.pdf'),
-- -- (9, 'ES6 Features', 'js-es6', 3, 3, NOW(), NOW(), 'lesson3.pdf'),
-- -- (10, 'Data Analysis with Pandas', 'pandas-analysis', 1, 4, NOW(), NOW(), 'lesson1.pdf'),
-- -- (11, 'NumPy Basics', 'numpy-basics', 2, 4, NOW(), NOW(), 'lesson2.pdf'),
-- -- (12, 'Building Fullstack App', 'fullstack-app', 1, 5, NOW(), NOW(), 'lesson1.pdf'),
-- -- (13, 'Frontend with React', 'frontend-react', 2, 5, NOW(), NOW(), 'lesson2.pdf'),
-- -- (14, 'Backend with Node.js', 'backend-node', 3, 5, NOW(), NOW(), 'lesson3.pdf');

-- -- -- USERS

-- -- -- COURSES
-- -- INSERT INTO courses_course (id, title, slug, description, created_at, updated_at) VALUES
-- -- (1, 'Python for Data', 'python-for-data', 'Learn Python from scratch', NOW(), NOW()),
-- -- (2, 'JavaScript Basics', 'javascript-basics', 'Intro to JS for web', NOW(), NOW());

-- -- -- LESSONS
-- -- INSERT INTO lessons_lesson (id, course_id, title, slug, content, created_at, updated_at) VALUES
-- -- (1, 1, 'Intro to Python', 'intro-python', 'Python basics content', NOW(), NOW()),
-- -- (2, 1, 'Python Data Types', 'python-data-types', 'Data types explained', NOW(), NOW()),
-- -- (3, 2, 'JS Syntax', 'js-syntax', 'Basics of JS syntax', NOW(), NOW());

-- -- -- BLOGS
-- -- INSERT INTO blogs_blog (id, title, content, author_id, created_at) VALUES
-- -- (1, 'Learning Python', 'Python is fun!', 1, NOW()),
-- -- (2, 'JS Tips', 'Use let and const wisely', 2, NOW());

-- -- -- COURSE ASSIGNMENTS
-- -- INSERT INTO courses_courseassignment (id, course_id, title, description, due_date) VALUES
-- -- (1, 1, 'Python Quiz 1', 'First quiz on Python basics', NOW() + INTERVAL '7 days'),
-- -- (2, 2, 'JS Assignment', 'Basic JS exercises', NOW() + INTERVAL '7 days');

-- -- -- TEACHERS
-- -- INSERT INTO teachers_teacherprofile (id, user_id, bio) VALUES
-- -- (1, 1, 'Python instructor'),
-- -- (2, 2, 'JS instructor');

-- -- -- TEACHER SCHEDULES
-- -- INSERT INTO teachers_schedule (id, teacher_id, day, start_time, end_time) VALUES
-- -- (1, 1, 'Monday', '10:00', '12:00'),
-- -- (2, 2, 'Tuesday', '14:00', '16:00');

-- -- -- TEACHER ASSIGNMENTS
-- -- INSERT INTO teachers_teacherassignment (id, teacher_id, course_id) VALUES
-- -- (1, 1, 1),
-- -- (2, 2, 2);

-- -- -- STUDENT ASSIGNMENTS SUBMISSIONS
-- -- INSERT INTO students_assignmentsubmission (id, student_id, assignment_id, submission_date, grade) VALUES
-- -- (1, 1, 1, NOW(), 85),
-- -- (2, 2, 2, NOW(), 90);

-- -- -- STUDENT ENROLLMENTS
-- -- INSERT INTO students_enrollment (id, student_id, course_id, enrolled_at) VALUES
-- -- (1, 1, 1, NOW()),
-- -- (2, 2, 2, NOW());

-- -- -- STUDENT EXAM PROGRESS
-- -- INSERT INTO students_examprogress (id, student_id, exam_id, score) VALUES
-- -- (1, 1, 1, 80),
-- -- (2, 2, 2, 75);

-- -- -- STUDENT PROFILES
-- -- INSERT INTO students_studentprofile (id, user_id, bio) VALUES
-- -- (1, 1, 'Python student'),
-- -- (2, 2, 'JS student');

-- -- -- EXAMS
-- -- INSERT INTO courses_exam (id, course_id, title, total_marks) VALUES
-- -- (1, 1, 'Python Midterm', 100),
-- -- (2, 2, 'JS Midterm', 100);

-- -- INSERT INTO exams_exam (id, title, total_marks) VALUES
-- -- (1, 'Final Python Exam', 100),
-- -- (2, 'Final JS Exam', 100);

-- -- INSERT INTO exams_examprogress (id, student_id, exam_id, score) VALUES
-- -- (1, 1, 1, 85),
-- -- (2, 2, 2, 90);

-- -- -- LESSON FEEDBACK
-- -- INSERT INTO lessons_lessonfeedback (id, lesson_id, student_id, feedback) VALUES
-- -- (1, 1, 1, 'Very helpful!'),
-- -- (2, 2, 2, 'Good explanations');

-- -- -- QUIZ OPTIONS
-- -- INSERT INTO lessons_quizoption (id, lesson_id, option_text, is_correct) VALUES
-- -- (1, 1, 'Option A', TRUE),
-- -- (2, 1, 'Option B', FALSE);

-- -- -- LESSON COMMENTS
-- -- INSERT INTO lessons_lessoncomment (id, lesson_id, student_id, comment) VALUES
-- -- (1, 1, 1, 'Nice lesson'),
-- -- (2, 2, 2, 'Clear content');

-- -- -- LESSON RESOURCES
-- -- INSERT INTO lessons_lessonresource (id, lesson_id, resource_url) VALUES
-- -- (1, 1, 'https://example.com/python-intro.pdf'),
-- -- (2, 2, 'https://example.com/python-datatypes.pdf');

-- -- -- LESSON PROGRESS
-- -- INSERT INTO lessons_lessonprogress (id, student_id, lesson_id, completed) VALUES
-- -- (1, 1, 1, TRUE),
-- -- (2, 2, 2, FALSE);

-- -- -- NOTIFICATIONS
-- -- INSERT INTO notifications_notification (id, user_id, message, created_at) VALUES
-- -- (1, 1, 'Welcome to Python course', NOW()),
-- -- (2, 2, 'Welcome to JS course', NOW());

-- -- -- PAYMENTS
-- -- INSERT INTO payments_transaction (id, user_id, amount, status, created_at) VALUES
-- -- (1, 1, 500, 'SUCCESS', NOW()),
-- -- (2, 2, 600, 'PENDING', NOW());

-- -- INSERT INTO payments_order (id, user_id, total_amount, status, created_at) VALUES
-- -- (1, 1, 500, 'PAID', NOW()),
-- -- (2, 2, 600, 'PENDING', NOW());

-- -- -- PROGRESS RESULTS
-- -- INSERT INTO progress_result (id, student_id, course_id, grade) VALUES
-- -- (1, 1, 1, 'A'),
-- -- (2, 2, 2, 'B');

-- -- INSERT INTO progress_lessonprogress (id, student_id, lesson_id, completed) VALUES
-- -- (1, 1, 1, TRUE),
-- -- (2, 2, 2, FALSE);

-- -- -- BLOG COMMENTS
-- -- INSERT INTO blogs_comment (id, blog_id, user_id, comment) VALUES
-- -- (1, 1, 1, 'Great article!'),
-- -- (2, 2, 2, 'Very informative!');


-- -- SELECT * FROM courses_course;
-- -- SELECT * FROM lessons_lesson;
-- -- SELECT * FROM users_customuser;
-- -- SELECT * FROM blogs_blog;
-- -- SELECT * FROM courses_courseassignment;
-- -- SELECT * FROM teachers_teacherprofile;
-- -- SELECT * FROM teachers_schedule;
-- -- SELECT * FROM teachers_teacherassignment;
-- -- SELECT * FROM students_assignmentsubmission;
-- -- SELECT * FROM students_enrollment;
-- -- SELECT * FROM students_examprogress;
-- -- SELECT * FROM students_studentprofile;
-- -- SELECT * FROM courses_exam;
-- -- SELECT * FROM courses_lesson;
-- -- SELECT * FROM exams_exam;
-- -- SELECT * FROM exams_examprogress;
-- -- SELECT * FROM lessons_lessonfeedback;
-- -- SELECT * FROM lessons_quizoption;
-- -- SELECT * FROM lessons_lessoncomment;
-- -- SELECT * FROM lessons_lessonresource;
-- -- SELECT * FROM lessons_lessonprogress;
-- -- SELECT * FROM notifications_notification;
-- -- SELECT * FROM payments_transaction;
-- -- SELECT * FROM payments_order;
-- -- SELECT * FROM progress_result;
-- -- SELECT * FROM progress_lessonprogress;
-- -- SELECT * FROM blogs_comment;
-- -- SELECT * FROM lessons_lesson;
-- -- SELECT * FROM courses_course;
-- -- SELECT * FROM lessons_lesson;
-- -- SELECT * FROM courses_course;
-- -- SELECT * FROM lessons_lesson;
-- -- SELECT * FROM courses_course;
-- -- SELECT * FROM lessons_lesson;
-- -- SELECT * FROM courses_course;
-- -- SELECT * FROM lessons_lesson;

















































-- -- Verify slugs
-- -- SELECT id, title, slug FROM courses_course;


-- -- SELECT id, title, slug
-- -- FROM lessons_lesson
-- -- WHERE slug IS NULL OR slug = '';
-- -- SELECT COUNT(*) FROM lessons_lesson;
-- -- SELECT id, title, slug 
-- -- FROM lessons_lesson;



-- -- UPDATE courses_course SET slug = 'full-stack-web-development' WHERE id = 2;
-- -- UPDATE courses_course SET slug = 'machine-learning-basics' WHERE id = 3;
-- -- UPDATE courses_course SET slug = 'data-structures-algorithms' WHERE id = 4;
-- -- UPDATE courses_course SET slug = 'intro-to-django' WHERE id = 5;



-- -- SELECT id, title, description
-- -- FROM courses_course
-- -- WHERE title = '' OR description = '' OR title IS NULL OR description IS NULL;


-- -- SELECT slug, COUNT(*) as total
-- -- FROM courses_course
-- -- GROUP BY slug
-- -- HAVING COUNT(*) > 1;




-- -- SELECT id, title, slug
-- -- FROM courses_course
-- -- WHERE slug IS NULL OR slug = '';


-- -- -- UPDATE courses_course 
-- -- -- SET slug = 'python-for-data-science'
-- -- -- WHERE id = 2;


-- -- -- -- Verify again
-- -- -- SELECT id, title, slug 
-- -- -- FROM courses_course 
-- -- -- WHERE id = 2;



-- -- SELECT * FROM courses_course;



-- -- SELECT id, title, slug, created_at
-- -- FROM courses_course
-- -- ORDER BY created_at DESC
-- -- LIMIT 5;
