-- SELECT id, title, slug
-- FROM courses_course
-- WHERE slug LIKE '%photoshop%';


SELECT * FROM users_customuser;



-- -- =====================================================
-- -- 📘 ELEARNING PROJECT — COURSE DATA INSERT SCRIPT
-- -- =====================================================
-- -- Author: Amit (InferX)
-- -- Purpose: Preload all course categories & lessons 
-- --          into the elearning database.
-- -- Tables: courses_course
-- -- =====================================================

-- -- ==============================
-- -- 🎨 Photoshop Course Lessons
-- -- ==============================
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

-- -- ==============================
-- -- ⚛️ Physics Courses
-- -- ==============================
-- INSERT INTO courses_course 
-- (created_at, updated_at, teacher_id, description, image, is_published, slug, title) 
-- VALUES
-- (NOW(), NOW(), NULL, 'Explore the universal law of gravitation and motion between celestial bodies.', 'physics-gravitation.png', TRUE, 'physics-gravitation', 'Physics — Gravitation'),
-- (NOW(), NOW(), NULL, 'Understand magnetic fields, electromagnetism, and their real-world applications.', 'physics-magnetism.png', TRUE, 'physics-magnetism', 'Physics — Magnetism'),
-- (NOW(), NOW(), NULL, 'Learn the principles of heat, temperature, and energy transfer.', 'physics-thermodynamics.png', TRUE, 'physics-thermodynamics', 'Physics — Thermodynamics'),
-- (NOW(), NOW(), NULL, 'Dive into the world of light, reflection, refraction, and optical instruments.', 'physics-optics.png', TRUE, 'physics-optics', 'Physics — Optics'),
-- (NOW(), NOW(), NULL, 'Study the structure and properties of atoms and subatomic particles.', 'physics-atoms.png', TRUE, 'physics-atoms', 'Physics — Atoms'),
-- (NOW(), NOW(), NULL, 'Understand modern physics — relativity, quantum theory, and nuclear science.', 'physics-modern.png', TRUE, 'physics-modern', 'Physics — Modern Physics');

-- -- ==============================
-- -- 🧪 Chemistry Courses
-- -- ==============================
-- INSERT INTO courses_course 
-- (created_at, updated_at, teacher_id, description, image, is_published, slug, title) 
-- VALUES
-- (NOW(), NOW(), NULL, 'Explore the study of carbon compounds, reactions, and mechanisms in organic chemistry.', 'chemistry-organic.png', TRUE, 'chemistry-organic', 'Chemistry — Organic'),
-- (NOW(), NOW(), NULL, 'Understand the laws of thermodynamics, kinetics, and equilibrium in physical chemistry.', 'chemistry-physical.png', TRUE, 'chemistry-physical', 'Chemistry — Physical'),
-- (NOW(), NOW(), NULL, 'Learn the foundational principles and basic concepts of chemistry.', 'chemistry-basicsconcepts.png', TRUE, 'chemistry-basicsconcepts', 'Chemistry — Basics Concepts'),
-- (NOW(), NOW(), NULL, 'Dive into the periodic table, atomic structure, and inorganic compounds.', 'chemistry-inorganic.png', TRUE, 'chemistry-inorganic', 'Chemistry — Inorganic'),
-- (NOW(), NOW(), NULL, 'Study the extraction and purification of metals through metallurgy processes.', 'chemistry-metallurgy.png', TRUE, 'chemistry-metallurgy', 'Chemistry — Metallurgy'),
-- (NOW(), NOW(), NULL, 'Explore biomolecules like carbohydrates, proteins, lipids, and nucleic acids.', 'chemistry-biomolecules.png', TRUE, 'chemistry-biomolecules', 'Chemistry — Biomolecules');

-- -- ==============================
-- -- 🧬 Biology Courses
-- -- ==============================
-- INSERT INTO courses_course 
-- (created_at, updated_at, teacher_id, description, image, is_published, slug, title) 
-- VALUES
-- (NOW(), NOW(), NULL, 'Understand human physiology and the functioning of organs and organ systems.', 'biology-physiology.png', TRUE, 'biology-physiology', 'Biology — Physiology'),
-- (NOW(), NOW(), NULL, 'Explore microorganisms, bacteria, viruses, and their role in ecosystems.', 'biology-microbiology.png', TRUE, 'biology-microbiology', 'Biology — Microbiology'),
-- (NOW(), NOW(), NULL, 'Study biodiversity, classification, and the variety of life on Earth.', 'biology-biodiversity.png', TRUE, 'biology-biodiversity', 'Biology — Biodiversity'),
-- (NOW(), NOW(), NULL, 'Dive into botany — the study of plants, their structure, and life processes.', 'biology-botany.png', TRUE, 'biology-botany', 'Biology — Botany'),
-- (NOW(), NOW(), NULL, 'Learn about zoology — the study of animals, their anatomy, and behavior.', 'biology-zoology.png', TRUE, 'biology-zoology', 'Biology — Zoology'),
-- (NOW(), NOW(), NULL, 'Understand the classification of living organisms into kingdoms and their evolution.', 'biology-kingdoms.png', TRUE, 'biology-kingdoms', 'Biology — Kingdoms');

-- -- ==============================
-- -- ➗ Mathematics Courses
-- -- ==============================
-- INSERT INTO courses_course 
-- (created_at, updated_at, teacher_id, description, image, is_published, slug, title) 
-- VALUES
-- (NOW(), NOW(), NULL, 'Explore the world of shapes, angles, and geometric reasoning.', 'mathematics-geometry.png', TRUE, 'mathematics-geometry', 'Mathematics — Geometry'),
-- (NOW(), NOW(), NULL, 'Master algebraic equations, expressions, and abstract relationships.', 'mathematics-algebra.png', TRUE, 'mathematics-algebra', 'Mathematics — Algebra'),
-- (NOW(), NOW(), NULL, 'Understand calculus — the study of limits, derivatives, and integrals.', 'mathematics-calculus.png', TRUE, 'mathematics-calculus', 'Mathematics — Calculus'),
-- (NOW(), NOW(), NULL, 'Learn about sets, relations, and foundational mathematical logic.', 'mathematics-set-relations.png', TRUE, 'mathematics-set-relations', 'Mathematics — Set & Relations'),
-- (NOW(), NOW(), NULL, 'Study trigonometric functions, identities, and their applications.', 'mathematics-trigonometry.png', TRUE, 'mathematics-trigonometry', 'Mathematics — Trigonometry'),
-- (NOW(), NOW(), NULL, 'Explore statistical data, probability, and mathematical predictions.', 'mathematics-statistics-probabilities.png', TRUE, 'mathematics-statistics-probabilities', 'Mathematics — Statistics & Probabilities');

-- -- ==============================
-- -- 🗣️ English Courses
-- -- ==============================
-- INSERT INTO courses_course 
-- (created_at, updated_at, teacher_id, description, image, is_published, slug, title) 
-- VALUES
-- (NOW(), NOW(), NULL, 'Build a strong foundation in English grammar — tenses, verbs, and sentence structures.', 'english-grammar.png', TRUE, 'english-grammar', 'English — Grammar'),
-- (NOW(), NOW(), NULL, 'Enhance your vocabulary, learn new words, idioms, and their effective usage.', 'english-vocabulary.png', TRUE, 'english-vocabulary', 'English — Vocabulary'),
-- (NOW(), NOW(), NULL, 'Develop reading comprehension skills and interpret written passages with accuracy.', 'english-reading-comprehension.png', TRUE, 'english-reading-comprehension', 'English — Reading Comprehension'),
-- (NOW(), NOW(), NULL, 'Improve your writing — from essays to professional communication.', 'english-writing-skills.png', TRUE, 'english-writing-skills', 'English — Writing Skills'),
-- (NOW(), NOW(), NULL, 'Master spoken English and pronunciation for confident communication.', 'english-speaking.png', TRUE, 'english-speaking', 'English — Speaking & Pronunciation'),
-- (NOW(), NOW(), NULL, 'Explore English literature — poetry, prose, and classic works of great authors.', 'english-literature.png', TRUE, 'english-literature', 'English — Literature');

-- -- ==============================
-- -- 💻 Programming / Web Development
-- -- ==============================
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

-- -- =====================================================
-- -- ✅ END OF INSERT SCRIPT
-- -- =====================================================


-- SELECT id, title, slug
-- FROM courses_course
-- WHERE slug LIKE 'photoshop%';


-- SELECT title, slug, course_id, order_index FROM lessons_lesson ORDER BY course_id, order_index;
-- SELECT 
--     id, 
--     title, 
--     slug, 
--     description, 
--     created_at, 
--     updated_at
-- FROM 
--     courses_course
-- ORDER BY 
--     id ASC;
