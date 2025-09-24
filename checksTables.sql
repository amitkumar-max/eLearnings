-- -- -- ✅ List all tables created by migrations

-- -- -- ✅ Check specific table ek ek karke
-- -- SELECT table_name 
-- -- FROM information_schema.tables 
-- -- WHERE table_schema = 'public'
-- --   AND table_name IN (
-- --     'users_customuser',
-- --     'students_studentprofile',
-- --     'students_enrollment',
-- --     'students_examprogress',
-- --     'students_assignmentsubmission',
-- --     'teachers_teacherprofile',
-- --     'teachers_teacherassignment',
-- --     'teachers_schedule',
-- --     'progress_result',
-- --     'progress_lessonprogress',
-- --     'payments_order',
-- --     'payments_transaction',
-- --     'notifications_notification',
-- --     'lessons_lesson',
-- --     'lessons_quizquestion',
-- --     'lessons_quizoption',
-- --     'lessons_lessonprogress',
-- --     'lessons_lessoncomment',
-- --     'lessons_lessonresource',
-- --     'lessons_lessonfeedback',
-- --     'exams_examprogress',
-- --     'exams_exam',
-- --     'courses_course',
-- --     'courses_lesson',
-- --     'courses_exam',
-- --     'courses_courseassignment',
-- --     'courses_enrollment',
-- --     'blogs_blog',
-- --     'blogs_comment',
-- --     'admin_adminprofile',
-- --     'admin_managedcourse',
-- --     'admin_adminpaymentlog',
-- --     'admin_adminnotification',
-- --     'admin_supportticket'
-- -- );


-- -- -- Insert dummy custom users
-- -- INSERT INTO custom_users (id, password, last_login, is_superuser, first_name, last_name, 
-- --                           is_staff, is_active, date_joined, email, full_name, role, address, 
-- --                           avatar, banner, bio, date_of_birth, is_verified, phone_number)
-- -- VALUES
-- -- (1, 'hashed_pw1', NOW(), TRUE,  'System',  'Admin',   TRUE,  TRUE,  NOW(), 'admin@example.com',   'System Admin',   'admin',   'HQ', NULL, NULL, 'Main admin user', '1990-01-01', TRUE,  '9999999999'),
-- -- (2, 'hashed_pw2', NOW(), FALSE, 'Alice',   'Teacher', TRUE,  TRUE,  NOW(), 'alice@school.com',   'Alice Teacher',  'teacher', 'Delhi', NULL, NULL, 'Maths teacher', '1985-05-10', TRUE,  '8888888888'),
-- -- (3, 'hashed_pw3', NOW(), FALSE, 'Bob',     'Student', FALSE, TRUE,  NOW(), 'bob@student.com',    'Bob Student',    'student', 'Mumbai', NULL, NULL, 'Loves coding', '2003-07-15', FALSE, '7777777777');


-- -- -- Insert dummy teachers
-- -- INSERT INTO teachers (id, name, email, subject, phone_number, created_at)
-- -- VALUES
-- -- (1, 'Alice Teacher', 'alice@school.com', 'Mathematics', '8888888888', NOW()),
-- -- (2, 'David Sir',     'david@school.com', 'Physics',     '7777777771', NOW()),
-- -- (3, 'Sophia Maam',   'sophia@school.com','Chemistry',   '6666666666', NOW());


-- -- -- Insert dummy courses
-- -- INSERT INTO courses_course (id, title, description, teacher_id, created_at, updated_at)
-- -- VALUES
-- -- (1, 'Mathematics 101', 'Basic algebra and geometry concepts', 1, NOW(), NOW()),
-- -- (2, 'Physics Fundamentals', 'Newton laws, mechanics and energy', 2, NOW(), NOW()),
-- -- (3, 'Chemistry Basics', 'Periodic table and bonding concepts', 3, NOW(), NOW());



-- --


-- -- ========================================
-- -- 1️⃣ users_customuser (students, teachers, admins)
-- -- ========================================
-- INSERT INTO users_customuser (email, full_name, role, password, is_staff, is_superuser, is_active)
-- VALUES
-- ('student1@example.com', 'Alice Student', 'student', 'password123', false, false, true),
-- ('student2@example.com', 'Bob Student', 'student', 'password123', false, false, true),
-- ('teacher1@example.com', 'Carol Teacher', 'teacher', 'password123', true, false, true),
-- ('teacher2@example.com', 'David Teacher', 'teacher', 'password123', true, false, true),
-- ('admin1@example.com', 'Eve Admin', 'admin', 'password123', true, true, true);

-- -- ========================================
-- -- 2️⃣ teachers_teacherprofile
-- -- ========================================
-- INSERT INTO teachers_teacherprofile (user_id, bio, statistics, awards, profile_views, social_links, created_at, updated_at)
-- VALUES
-- (3, 'Expert in Python and Data Science', '{}', '["Best Teacher 2024"]', 120, '{}', NOW(), NOW()),
-- (4, 'Frontend & UI/UX specialist', '{}', '["UI Award 2023"]', 85, '{}', NOW(), NOW());

-- -- ========================================
-- -- 3️⃣ teachers_teacherassignment
-- -- ========================================
-- INSERT INTO teachers_teacherassignment (teacher_id, course_id, title, description, due_date, created_at, updated_at)
-- VALUES
-- (1, 1, 'Assignment 1', 'Introduction assignment', NOW(), NOW(), NOW()),
-- (1, 1, 'Assignment 2', 'Intermediate assignment', NOW(), NOW(), NOW()),
-- (2, 2, 'UI Project', 'Design a landing page', NOW(), NOW(), NOW());

-- -- ========================================
-- -- 4️⃣ teachers_schedule
-- -- ========================================
-- INSERT INTO teachers_schedule (teacher_id, course_id, date, time, topic, created_at, updated_at)
-- VALUES
-- (1, 1, NOW(), '10:00', 'Python Basics', NOW(), NOW()),
-- (1, 1, NOW(), '14:00', 'OOP Concepts', NOW(), NOW()),
-- (2, 2, NOW(), '11:00', 'CSS Grid', NOW(), NOW());

-- -- ========================================
-- -- 5️⃣ students_studentprofile
-- -- ========================================
-- INSERT INTO students_studentprofile (user_id, bio, progress, exam_scores, assignments_submitted, last_login_ip, points, achievements)
-- VALUES
-- (1, 'Eager to learn Python', '{}', '{}', '{}', '127.0.0.1', 10, '[]'),
-- (2, 'Math lover', '{}', '{}', '{}', '127.0.0.2', 15, '[]');

-- -- ========================================
-- -- 6️⃣ students_enrollment
-- -- ========================================
-- INSERT INTO students_enrollment (student_id, course_id, date_enrolled, progress, created_at, updated_at)
-- VALUES
-- (1, 1, NOW(), '{}', NOW(), NOW()),
-- (2, 2, NOW(), '{}', NOW(), NOW());

-- -- ========================================
-- -- 7️⃣ students_examprogress
-- -- ========================================
-- INSERT INTO students_examprogress (student_id, exam_id, completed, score)
-- VALUES
-- (1, 1, false, 0),
-- (2, 2, true, 88.5);

-- -- ========================================
-- -- 8️⃣ students_assignmentsubmission
-- -- ========================================
-- INSERT INTO students_assignmentsubmission (student_id, exam_id, submitted_at, score, status)
-- VALUES
-- (1, 1, NOW(), 75.0, 'submitted'),
-- (2, 2, NOW(), 92.0, 'graded');

-- -- ========================================
-- -- 9️⃣ progress_result
-- -- ========================================
-- INSERT INTO progress_result (user_id, lesson_id, score, completed)
-- VALUES
-- (1, 1, 80, true),
-- (2, 2, 60, false);

-- -- ========================================
-- -- 10️⃣ progress_lessonprogress
-- -- ========================================
-- INSERT INTO progress_lessonprogress (student_id, lesson_id)
-- VALUES
-- (1, 1),
-- (2, 2);

-- -- ========================================
-- -- 11️⃣ payments_order
-- -- ========================================
-- INSERT INTO payments_order (user_id, course_id, currency, amount, status, meta, created_at, updated_at)
-- VALUES
-- (1, 1, 'INR', 699.00, 'paid', '{}', NOW(), NOW()),
-- (2, 2, 'INR', 899.00, 'pending', '{}', NOW(), NOW());

-- -- ========================================
-- -- 12️⃣ payments_transaction
-- -- ========================================
-- INSERT INTO payments_transaction (order_id, gateway, amount, currency, status, created_at, updated_at)
-- VALUES
-- (1, 'razorpay', 699.00, 'INR', 'success', NOW(), NOW()),
-- (2, 'razorpay', 899.00, 'INR', 'initiated', NOW(), NOW());

-- -- ========================================
-- -- 13️⃣ notifications_notification
-- -- ========================================
-- INSERT INTO notifications_notification (user_id, title, message, notification_type, is_read, created_at)
-- VALUES
-- (1, 'Welcome!', 'Welcome to the platform', 'INFO', false, NOW()),
-- (2, 'Exam Reminder', 'Your exam starts tomorrow', 'WARNING', false, NOW());

-- -- ========================================
-- -- 14️⃣ lessons_lesson
-- -- ========================================
-- INSERT INTO lessons_lesson (course_id, title, content, created_at, updated_at)
-- VALUES
-- (1, 'Python Basics', 'Introduction to Python', NOW(), NOW()),
-- (2, 'CSS Fundamentals', 'Learn CSS basics', NOW(), NOW());

-- -- ========================================
-- -- 15️⃣ lessons_quizquestion
-- -- ========================================
-- INSERT INTO lessons_quizquestion (lesson_id, question_text)
-- VALUES
-- (1, 'What is Python?'),
-- (2, 'Which property sets background color?');

-- -- ========================================
-- -- 16️⃣ lessons_quizoption
-- -- ========================================
-- INSERT INTO lessons_quizoption (question_id, option_text, is_correct)
-- VALUES
-- (1, 'Programming Language', true),
-- (1, 'Snake', false),
-- (2, 'background-color', true),
-- (2, 'color', false);

-- -- ========================================
-- -- 17️⃣ lessons_lessoncomment
-- -- ========================================
-- INSERT INTO lessons_lessoncomment (user_id, lesson_id, comment, created_at)
-- VALUES
-- (1, 1, 'Great lesson!', NOW()),
-- (2, 2, 'Very helpful', NOW());

-- -- ========================================
-- -- 18️⃣ lessons_lessonresource
-- -- ========================================
-- INSERT INTO lessons_lessonresource (lesson_id, file)
-- VALUES
-- (1, 'resources/python_intro.pdf'),
-- (2, 'resources/css_basics.pdf');

-- -- ========================================
-- -- 19️⃣ lessons_lessonfeedback
-- -- ========================================
-- INSERT INTO lessons_lessonfeedback (user_id, lesson_id, feedback, created_at)
-- VALUES
-- (1, 1, 'Loved the content', NOW()),
-- (2, 2, 'Could be more detailed', NOW());

-- -- ========================================
-- -- 20️⃣ exams_exam
-- -- ========================================
-- INSERT INTO exams_exam (course_id, title, date, created_at, updated_at)
-- VALUES
-- (1, 'Python Basics Exam', NOW(), NOW(), NOW()),
-- (2, 'CSS Fundamentals Exam', NOW(), NOW(), NOW());

-- -- ========================================
-- -- 21️⃣ exams_examprogress
-- -- ========================================
-- INSERT INTO exams_examprogress (student_id, exam_id, score, completed, started_at, finished_at)
-- VALUES
-- (1, 1, 75, true, NOW(), NOW()),
-- (2, 2, 88, false, NOW(), NULL);

-- -- ========================================
-- -- 22️⃣ courses_course
-- -- ========================================
-- INSERT INTO courses_course (title, description, image, slug, is_published, teacher_id, created_at, updated_at)
-- VALUES
-- ('Python for Beginners', 'Learn Python from scratch', NULL, 'python-for-beginners', true, 3, NOW(), NOW()),
-- ('CSS Basics', 'Learn CSS', NULL, 'css-basics', true, 4, NOW(), NOW());

-- -- ========================================
-- -- 23️⃣ courses_lesson
-- -- ========================================
-- INSERT INTO courses_lesson (course_id, title, content, created_at, updated_at)
-- VALUES
-- (1, 'Intro Python', 'Python Basics Content', NOW(), NOW()),
-- (2, 'Intro CSS', 'CSS Basics Content', NOW(), NOW());

-- -- ========================================
-- -- 24️⃣ courses_exam
-- -- ========================================
-- INSERT INTO courses_exam (course_id, title, date, created_at, updated_at)
-- VALUES
-- (1, 'Python Final Exam', NOW(), NOW(), NOW()),
-- (2, 'CSS Final Exam', NOW(), NOW(), NOW());

-- -- ========================================
-- -- 25️⃣ courses_courseassignment
-- -- ========================================
-- INSERT INTO courses_courseassignment (course_id, title, description, due_date, created_at, updated_at)
-- VALUES
-- (1, 'Python Assignment', 'Practice problems', NOW(), NOW(), NOW()),
-- (2, 'CSS Assignment', 'Create a layout', NOW(), NOW(), NOW());

-- -- ========================================
-- -- 26️⃣ courses_enrollment
-- -- ========================================
-- INSERT INTO courses_enrollment (student_id, course_id, date_enrolled, created_at, updated_at)
-- VALUES
-- (1, 1, NOW(), NOW(), NOW()),
-- (2, 2, NOW(), NOW(), NOW());

-- -- ========================================
-- -- 27️⃣ blogs_blog
-- -- ========================================
-- INSERT INTO blogs_blog (title, content, author_id, created_at, updated_at)
-- VALUES
-- ('Getting Started with Python', 'Introductory content', 3, NOW(), NOW()),
-- ('CSS Tips & Tricks', 'Advanced CSS content', 4, NOW(), NOW());

-- -- ========================================
-- -- 28️⃣ blogs_comment
-- -- ========================================
-- INSERT INTO blogs_comment (blog_id, user_id, content, created_at)
-- VALUES
-- (1, 1, 'Very helpful blog', NOW()),
-- (2, 2, 'Loved the tips', NOW());



-- -- ========================================
-- -- 29️⃣ admin_adminprofile
-- -- ========================================
-- INSERT INTO admin_adminprofile (user_id, permissions_notes, managed_sections, last_login_ip, super_admin)
-- VALUES
-- (5, 'Full access to all modules', '["users","courses","payments"]', '127.0.0.5', true),
-- (5, 'Limited access to courses and students', '["courses","students"]', '127.0.0.5', false);

-- -- ========================================
-- -- 30️⃣ admin_managedcourse
-- -- ========================================
-- INSERT INTO admin_managedcourse (admin_id, course_name, created_at, approved)
-- VALUES
-- (1, 'Python for Beginners', NOW(), true),
-- (1, 'CSS Basics', NOW(), false),
-- (1, 'JavaScript Advanced', NOW(), true);

-- -- ========================================
-- -- 31️⃣ admin_adminpaymentlog
-- -- ========================================
-- INSERT INTO admin_adminpaymentlog (admin_id, amount, student_name, course_name, timestamp, status)
-- VALUES
-- (1, 699.00, 'Alice Student', 'Python for Beginners', NOW(), 'completed'),
-- (1, 899.00, 'Bob Student', 'CSS Basics', NOW(), 'pending');

-- -- ========================================
-- -- 32️⃣ admin_adminnotification
-- -- ========================================
-- INSERT INTO admin_adminnotification (admin_id, title, message, created_at, is_active)
-- VALUES
-- (1, 'System Update', 'Server maintenance scheduled', NOW(), true),
-- (1, 'New Course Approval', 'Please approve pending courses', NOW(), true);

-- -- ========================================
-- -- 33️⃣ admin_supportticket
-- -- ========================================
-- INSERT INTO supportticket (admin_id, student_name, message, resolved, created_at)
-- VALUES
-- (1, 'Alice Student', 'Cannot access course materials', false, NOW()),
-- (1, 'Bob Student', 'Payment not reflected', true, NOW());


-- INSERT INTO users_customuser
-- (email, password, full_name, first_name, last_name, role, is_staff, is_superuser, is_active, date_joined, is_verified)
-- VALUES
-- ('alice@example.com', 'hashed_password_here', 'Alice Student', 'Alice', 'Student', 'student', false, false, true, NOW(), true);



SELECT * FROM public.admin_adminprofile;
