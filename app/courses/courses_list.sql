-- SELECT *
-- FROM courses_course
-- ORDER BY id ASC;
-- INSERT INTO courses_course (title, slug, description, created_at, updated_at, is_published) VALUES
-- ('Lesson_1_Into', 'lesson_1_into', 'Photoshop basics course module lesson or effect.', '2025-10-22 05:49:30.428866+00', '2025-10-22 05:49:30.428866+00', TRUE),
-- ('Lesson_2_Tools_And_Techniques', 'lesson_2_tools_and_techniques', 'Photoshop basics course module lesson or effect.', '2025-10-22 05:49:31.500653+00', '2025-10-22 05:49:31.500653+00', TRUE),
-- ('Introduction', 'photoshop-basics-introduction', 'Photoshop basics course module lesson or effect.', '2025-10-27 03:27:01.493888+00', '2025-10-27 03:27:01.493888+00', TRUE),
-- ('3D Collage Effect', 'photoshop-basics-3d-collage-effect', 'Photoshop basics course module lesson or effect.', '2025-10-27 13:17:30.383311+00', '2025-10-27 13:17:30.383311+00', TRUE),
-- ('Bubble Effect', 'photoshop-basics-bubble-effect', 'Photoshop basics course module lesson or effect.', '2025-10-27 13:17:31.920738+00', '2025-10-27 13:17:31.920738+00', TRUE),
-- ('Cloud Face', 'photoshop-basics-cloud-face', 'Photoshop basics course module lesson or effect.', '2025-10-27 13:17:33.874536+00', '2025-10-27 13:17:33.874536+00', TRUE),
-- ('Dispersion Effect', 'photoshop-basics-dispersion-effect', 'Photoshop basics course module lesson or effect.', '2025-10-27 13:17:35.754399+00', '2025-10-27 13:17:35.754399+00', TRUE),
-- ('Eye Blending Effect', 'photoshop-basics-eye-blending-effect', 'Photoshop basics course module lesson or effect.', '2025-10-27 13:17:37.553205+00', '2025-10-27 13:17:37.553205+00', TRUE),
-- ('Headlight Blinking Effect', 'photoshop-basics-headlight-blinking-effect', 'Photoshop basics course module lesson or effect.', '2025-10-27 13:17:39.199647+00', '2025-10-27 13:17:39.199647+00', TRUE),
-- ('Lesson 1 Into', 'photoshop-basics-lesson_1_into', 'Photoshop basics course module lesson or effect.', '2025-10-27 13:17:41.764517+00', '2025-10-27 13:17:41.764517+00', TRUE),
-- ('Lesson 2 Tools And Techniques', 'photoshop-basics-lesson_2_tools_and_techniques', 'Photoshop basics course module lesson or effect.', '2025-10-27 13:17:43.492319+00', '2025-10-27 13:17:43.492319+00', TRUE),
-- ('Reflection Effect', 'photoshop-basics-reflection-effect', 'Photoshop basics course module lesson or effect.', '2025-10-27 13:17:45.034845+00', '2025-10-27 13:17:45.034845+00', TRUE),
-- ('Slice Head', 'photoshop-basics-slice-head', 'Photoshop basics course module lesson or effect.', '2025-10-27 13:17:46.664710+00', '2025-10-27 13:17:46.664710+00', TRUE);
-- SELECT title, slug FROM courses_course WHERE slug LIKE 'photoshop%';
-- UPDATE courses_course SET slug = 'photoshop-basics' WHERE title = 'Photoshop Basics';
-- SELECT *
-- FROM lessons_lesson
-- ORDER BY course_id, id ASC;
-- INSERT INTO courses_course (title, slug, description, is_published, created, modified)
-- SELECT DISTINCT title, slug, 'Auto-created from lessons', TRUE, NOW(), NOW()
-- FROM lessons_lesson
-- WHERE slug NOT IN (SELECT slug FROM courses_course);
-- INSERT INTO courses_course (title, slug, description, is_published, created_at, updated_at)
-- SELECT DISTINCT title, slug, 'Auto-created from lessons', TRUE, NOW(), NOW()
-- FROM lessons_lesson
-- WHERE slug NOT IN (SELECT slug FROM courses_course);
-- INSERT INTO courses_course (title, slug, description, is_published, created_at, updated_at)
-- SELECT DISTINCT
--     title,
--     LEFT(slug, 50),  -- Trim to 50 chars
--     'Auto-created from lessons',
--     TRUE,
--     NOW(),
--     NOW()
-- FROM lessons_lesson
-- WHERE LEFT(slug, 50) NOT IN (SELECT slug FROM courses_course);
-- SELECT 
--     l.id AS lesson_id,
--     l.title AS lesson_title,
--     l.slug AS lesson_slug,
--     c.title AS course_title,
--     c.slug AS course_slug
-- FROM lessons_lesson l
-- JOIN coursecs_course c ON l.course_id = c.id
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











