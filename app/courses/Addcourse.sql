-- INSERT INTO courses_course
-- (created_at, updated_at, teacher_id, description, image, is_published, slug, title)
-- VALUES
-- (NOW(), NOW(), NULL, 'Learn kinematics concepts in physics — motion, velocity, and acceleration', 'physics.png', TRUE, 'physics-kinematics', 'Physics Kinematics');

SELECT id FROM courses_course WHERE slug = 'physics-kinematics';
INSERT INTO lessons_lesson (created_at, updated_at, course_id, title, slug, order_index)
VALUES
(NOW(), NOW(), 35, 'Introduction', 'introduction', 1),
(NOW(), NOW(), 35, 'Content', 'content', 2),
(NOW(), NOW(), 35, 'Conclusion', 'conclusion', 3);
