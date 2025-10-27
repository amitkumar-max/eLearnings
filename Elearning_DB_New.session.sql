SELECT * FROM django_migrations;
-- SQLTools me run
-- INSERT INTO django_migrations (app, name, applied)
-- VALUES ('users','0001_initial', now());




-- SELECT * FROM django_migrations;



-- \dt users*

-- SELECT tablename 
-- FROM pg_tables 
-- WHERE schemaname = 'public' AND tablename LIKE 'users%';



-- SELECT table_name
-- FROM information_schema.tables
-- WHERE table_schema = 'public'
-- ORDER BY table_name;


-- SELECT 
--     table_name, 
--     (xpath('/row/cnt/text()', xml_count))[1]::text::int AS row_count
-- FROM (
--     SELECT 
--         table_name,
--         query_to_xml(format('SELECT count(*) AS cnt FROM %I', table_name), false, true, '') AS xml_count
--     FROM information_schema.tables
--     WHERE table_schema = 'public'
-- ) t
-- ORDER BY row_count DESC;


-- SELECT 
--     table_name, 
--     column_name, 
--     data_type, 
--     is_nullable
-- FROM information_schema.columns
-- WHERE table_schema = 'public'
-- ORDER BY table_name, ordinal_position;

-- SELECT 
--     pg_database.datname AS database_name,
--     pg_size_pretty(pg_database_size(pg_database.datname)) AS size
-- FROM pg_database
-- WHERE datname NOT IN ('template0', 'template1')
-- ORDER BY pg_database_size(pg_database.datname) DESC;


-- SELECT * FROM auth_permission LIMIT 10;

-- SELECT id, title, description, created_at, updated_at 
-- FROM courses_course
-- ORDER BY id DESC
-- LIMIT 10;

-- SELECT id, student_id, course_id, enrollment_date, progress
-- FROM students_enrollment
-- ORDER BY id DESC
-- LIMIT 10;

-- SELECT id, title, course_id, video_url, duration, created_at
-- FROM lessons_lesson
-- ORDER BY id DESC
-- LIMIT 10;

-- SELECT l.title, c.title AS course_name
-- FROM lessons_lesson l
-- JOIN courses_course c ON l.course_id = c.id
-- LIMIT 10;

-- SELECT * FROM django_migrations ORDER BY id DESC LIMIT 10;


-- SELECT * FROM django_content_type;

-- SELECT id, course_id, student_id, views, likes, comments_count
-- FROM courses_courseinteraction
-- ORDER BY id DESC
-- LIMIT 10;

-- SELECT id, username, email, is_staff, is_active, date_joined
-- FROM users_customuser
-- ORDER BY id DESC
-- LIMIT 10;


-- SELECT id, user_id, bio, total_courses_enrolled, achievements
-- FROM students_studentprofile
-- ORDER BY id DESC
-- LIMIT 10;


-- SELECT * FROM django_session;



SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'courses_course';


-- For each:
SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'students_enrollment';
SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'lessons_lesson';
SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'courses_courseinteraction';
SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'users_customuser';
SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'students_studentprofile';



