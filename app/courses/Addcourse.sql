-- -- INSERT INTO courses_course
-- -- (created_at, updated_at, teacher_id, description, image, is_published, slug, title)
-- -- VALUES
-- -- (NOW(), NOW(), NULL, 'Learn kinematics concepts in physics — motion, velocity, and acceleration', 'physics.png', TRUE, 'physics-kinematics', 'Physics Kinematics');

-- SELECT id FROM courses_course WHERE slug = 'physics-kinematics';
-- INSERT INTO lessons_lesson (created_at, updated_at, course_id, title, slug, order_index)
-- VALUES
-- (NOW(), NOW(), 35, 'Introduction', 'introduction', 1),
-- (NOW(), NOW(), 35, 'Content', 'content', 2),
-- (NOW(), NOW(), 35, 'Conclusion', 'conclusion', 3);


-- SELECT 
--     c.id AS course_id,
--     c.title AS course_title,
--     c.slug AS course_slug,
--     l.id AS lesson_id,
--     l.title AS lesson_title,
--     l.slug AS lesson_slug,
--     l.order_index,
--     l.content_file
-- FROM courses_course c
-- LEFT JOIN lessons_lesson l ON c.id = l.course_id
-- ORDER BY c.id, l.order_index;


-- SELECT * FROM courses_course;
-- SELECT * FROM lessons_lesson;

-- INSERT INTO courses_course 
-- (created_at, updated_at, teacher_id, description, image, is_published, slug, title) 
-- VALUES
-- (NOW(), NOW(), NULL, 'Explore the universal law of gravitation and motion between celestial bodies.', 'physics-gravitation.png', TRUE, 'physics-gravitation', 'Physics — Gravitation'),
-- (NOW(), NOW(), NULL, 'Understand magnetic fields, electromagnetism, and their real-world applications.', 'physics-magnetism.png', TRUE, 'physics-magnetism', 'Physics — Magnetism'),
-- (NOW(), NOW(), NULL, 'Learn the principles of heat, temperature, and energy transfer.', 'physics-thermodynamics.png', TRUE, 'physics-thermodynamics', 'Physics — Thermodynamics'),
-- (NOW(), NOW(), NULL, 'Dive into the world of light, reflection, refraction, and optical instruments.', 'physics-optics.png', TRUE, 'physics-optics', 'Physics — Optics'),
-- (NOW(), NOW(), NULL, 'Study the structure and properties of atoms and subatomic particles.', 'physics-atoms.png', TRUE, 'physics-atoms', 'Physics — Atoms'),
-- (NOW(), NOW(), NULL, 'Understand modern physics — relativity, quantum theory, and nuclear science.', 'physics-modern.png', TRUE, 'physics-modern', 'Physics — Modern Physics');


-- INSERT INTO lessons_lesson 
-- (title, slug, order_index, course_id, created_at, updated_at, content_file)
-- VALUES
-- ('Introduction to Gravitation', 'physics-gravitation-intro', 36, (SELECT id FROM courses_course WHERE slug='physics-gravitation'), NOW(), NOW(), 'physics-gravitation-intro.txt'),
-- ('Introduction to Magnetism', 'physics-magnetism-intro', 37, (SELECT id FROM courses_course WHERE slug='physics-magnetism'), NOW(), NOW(), 'physics-magnetism-intro.txt'),
-- ('Introduction to Thermodynamics', 'physics-thermodynamics-intro', 38, (SELECT id FROM courses_course WHERE slug='physics-thermodynamics'), NOW(), NOW(), 'physics-thermodynamics-intro.txt'),
-- ('Introduction to Optics', 'physics-optics-intro', 39, (SELECT id FROM courses_course WHERE slug='physics-optics'), NOW(), NOW(), 'physics-optics-intro.txt'),
-- ('Introduction to Atoms', 'physics-atoms-intro', 40, (SELECT id FROM courses_course WHERE slug='physics-atoms'), NOW(), NOW(), 'physics-atoms-intro.txt'),
-- ('Introduction to Modern Physics', 'physics-modern-intro', 41, (SELECT id FROM courses_course WHERE slug='physics-modern'), NOW(), NOW(), 'physics-modern-intro.txt');

-- INSERT INTO courses_course 
-- (created_at, updated_at, teacher_id, description, image, is_published, slug, title) 
-- VALUES
-- (NOW(), NOW(), NULL, 'Explore the study of carbon compounds, reactions, and mechanisms in organic chemistry.', 'chemistry-organic.png', TRUE, 'chemistry-organic', 'Chemistry — Organic'),
-- (NOW(), NOW(), NULL, 'Understand the laws of thermodynamics, kinetics, and equilibrium in physical chemistry.', 'chemistry-physical.png', TRUE, 'chemistry-physical', 'Chemistry — Physical'),
-- (NOW(), NOW(), NULL, 'Learn the foundational principles and basic concepts of chemistry.', 'chemistry-basicsconcepts.png', TRUE, 'chemistry-basicsconcepts', 'Chemistry — Basics Concepts'),
-- (NOW(), NOW(), NULL, 'Dive into the periodic table, atomic structure, and inorganic compounds.', 'chemistry-inorganic.png', TRUE, 'chemistry-inorganic', 'Chemistry — Inorganic'),
-- (NOW(), NOW(), NULL, 'Study the extraction and purification of metals through metallurgy processes.', 'chemistry-metallurgy.png', TRUE, 'chemistry-metallurgy', 'Chemistry — Metallurgy'),
-- (NOW(), NOW(), NULL, 'Explore biomolecules like carbohydrates, proteins, lipids, and nucleic acids.', 'chemistry-biomolecules.png', TRUE, 'chemistry-biomolecules', 'Chemistry — Biomolecules');

-- INSERT INTO lessons_lesson 
-- (title, slug, order_index, course_id, created_at, updated_at, content_file)
-- VALUES
-- ('Introduction to Organic Chemistry', 'chemistry-organic-intro', 42, (SELECT id FROM courses_course WHERE slug='chemistry-organic'), NOW(), NOW(), 'chemistry-organic-intro.txt'),
-- ('Introduction to Physical Chemistry', 'chemistry-physical-intro', 43, (SELECT id FROM courses_course WHERE slug='chemistry-physical'), NOW(), NOW(), 'chemistry-physical-intro.txt'),
-- ('Introduction to Basic Concepts of Chemistry', 'chemistry-basicsconcepts-intro', 44, (SELECT id FROM courses_course WHERE slug='chemistry-basicsconcepts'), NOW(), NOW(), 'chemistry-basicsconcepts-intro.txt'),
-- ('Introduction to Inorganic Chemistry', 'chemistry-inorganic-intro', 45, (SELECT id FROM courses_course WHERE slug='chemistry-inorganic'), NOW(), NOW(), 'chemistry-inorganic-intro.txt'),
-- ('Introduction to Metallurgy', 'chemistry-metallurgy-intro', 46, (SELECT id FROM courses_course WHERE slug='chemistry-metallurgy'), NOW(), NOW(), 'chemistry-metallurgy-intro.txt'),
-- ('Introduction to Biomolecules', 'chemistry-biomolecules-intro', 47, (SELECT id FROM courses_course WHERE slug='chemistry-biomolecules'), NOW(), NOW(), 'chemistry-biomolecules-intro.txt');


-- INSERT INTO courses_course 
-- (created_at, updated_at, teacher_id, description, image, is_published, slug, title) 
-- VALUES
-- (NOW(), NOW(), NULL, 'Understand human physiology and the functioning of organs and organ systems.', 'biology-physiology.png', TRUE, 'biology-physiology', 'Biology — Physiology'),
-- (NOW(), NOW(), NULL, 'Explore microorganisms, bacteria, viruses, and their role in ecosystems.', 'biology-microbiology.png', TRUE, 'biology-microbiology', 'Biology — Microbiology'),
-- (NOW(), NOW(), NULL, 'Study biodiversity, classification, and the variety of life on Earth.', 'biology-biodiversity.png', TRUE, 'biology-biodiversity', 'Biology — Biodiversity'),
-- (NOW(), NOW(), NULL, 'Dive into botany — the study of plants, their structure, and life processes.', 'biology-botany.png', TRUE, 'biology-botany', 'Biology — Botany'),
-- (NOW(), NOW(), NULL, 'Learn about zoology — the study of animals, their anatomy, and behavior.', 'biology-zoology.png', TRUE, 'biology-zoology', 'Biology — Zoology'),
-- (NOW(), NOW(), NULL, 'Understand the classification of living organisms into kingdoms and their evolution.', 'biology-kingdoms.png', TRUE, 'biology-kingdoms', 'Biology — Kingdoms');

-- INSERT INTO lessons_lesson 
-- (title, slug, order_index, course_id, created_at, updated_at, content_file)
-- VALUES
-- ('Introduction to Physiology', 'biology-physiology-intro', 48, (SELECT id FROM courses_course WHERE slug='biology-physiology'), NOW(), NOW(), 'biology-physiology-intro.txt'),
-- ('Introduction to Microbiology', 'biology-microbiology-intro', 49, (SELECT id FROM courses_course WHERE slug='biology-microbiology'), NOW(), NOW(), 'biology-microbiology-intro.txt'),
-- ('Introduction to Biodiversity', 'biology-biodiversity-intro', 50, (SELECT id FROM courses_course WHERE slug='biology-biodiversity'), NOW(), NOW(), 'biology-biodiversity-intro.txt'),
-- ('Introduction to Botany', 'biology-botany-intro', 51, (SELECT id FROM courses_course WHERE slug='biology-botany'), NOW(), NOW(), 'biology-botany-intro.txt'),
-- ('Introduction to Zoology', 'biology-zoology-intro', 52, (SELECT id FROM courses_course WHERE slug='biology-zoology'), NOW(), NOW(), 'biology-zoology-intro.txt'),
-- ('Introduction to Kingdoms', 'biology-kingdoms-intro', 53, (SELECT id FROM courses_course WHERE slug='biology-kingdoms'), NOW(), NOW(), 'biology-kingdoms-intro.txt');



-- INSERT INTO courses_course 
-- (created_at, updated_at, teacher_id, description, image, is_published, slug, title) 
-- VALUES
-- (NOW(), NOW(), NULL, 'Explore the world of shapes, angles, and geometric reasoning.', 'mathematics-geometry.png', TRUE, 'mathematics-geometry', 'Mathematics — Geometry'),
-- (NOW(), NOW(), NULL, 'Master algebraic equations, expressions, and abstract relationships.', 'mathematics-algebra.png', TRUE, 'mathematics-algebra', 'Mathematics — Algebra'),
-- (NOW(), NOW(), NULL, 'Understand calculus — the study of limits, derivatives, and integrals.', 'mathematics-calculus.png', TRUE, 'mathematics-calculus', 'Mathematics — Calculus'),
-- (NOW(), NOW(), NULL, 'Learn about sets, relations, and foundational mathematical logic.', 'mathematics-set-relations.png', TRUE, 'mathematics-set-relations', 'Mathematics — Set & Relations'),
-- (NOW(), NOW(), NULL, 'Study trigonometric functions, identities, and their applications.', 'mathematics-trigonometry.png', TRUE, 'mathematics-trigonometry', 'Mathematics — Trigonometry'),
-- (NOW(), NOW(), NULL, 'Explore statistical data, probability, and mathematical predictions.', 'mathematics-statistics-probabilities.png', TRUE, 'mathematics-statistics-probabilities', 'Mathematics — Statistics & Probabilities');

-- INSERT INTO lessons_lesson 
-- (title, slug, order_index, course_id, created_at, updated_at, content_file)
-- VALUES
-- ('Introduction to Geometry', 'mathematics-geometry-intro', 54, (SELECT id FROM courses_course WHERE slug='mathematics-geometry'), NOW(), NOW(), 'mathematics-geometry-intro.txt'),
-- ('Introduction to Algebra', 'mathematics-algebra-intro', 55, (SELECT id FROM courses_course WHERE slug='mathematics-algebra'), NOW(), NOW(), 'mathematics-algebra-intro.txt'),
-- ('Introduction to Calculus', 'mathematics-calculus-intro', 56, (SELECT id FROM courses_course WHERE slug='mathematics-calculus'), NOW(), NOW(), 'mathematics-calculus-intro.txt'),
-- ('Introduction to Set & Relations', 'mathematics-set-relations-intro', 57, (SELECT id FROM courses_course WHERE slug='mathematics-set-relations'), NOW(), NOW(), 'mathematics-set-relations-intro.txt'),
-- ('Introduction to Trigonometry', 'mathematics-trigonometry-intro', 58, (SELECT id FROM courses_course WHERE slug='mathematics-trigonometry'), NOW(), NOW(), 'mathematics-trigonometry-intro.txt'),
-- ('Introduction to Statistics & Probabilities', 'mathematics-statistics-probabilities-intro', 59, (SELECT id FROM courses_course WHERE slug='mathematics-statistics-probabilities'), NOW(), NOW(), 'mathematics-statistics-probabilities-intro.txt');

-- INSERT INTO courses_course 
-- (created_at, updated_at, teacher_id, description, image, is_published, slug, title) 
-- VALUES
-- (NOW(), NOW(), NULL, 'Explore the study of carbon compounds, reactions, and mechanisms in organic chemistry.', 'chemistry-organic.png', TRUE, 'chemistry-organic', 'Chemistry — Organic'),
-- (NOW(), NOW(), NULL, 'Understand the laws of thermodynamics, kinetics, and equilibrium in physical chemistry.', 'chemistry-physical.png', TRUE, 'chemistry-physical', 'Chemistry — Physical'),
-- (NOW(), NOW(), NULL, 'Learn the foundational principles and basic concepts of chemistry.', 'chemistry-basicsconcepts.png', TRUE, 'chemistry-basicsconcepts', 'Chemistry — Basics Concepts'),
-- (NOW(), NOW(), NULL, 'Dive into the periodic table, atomic structure, and inorganic compounds.', 'chemistry-inorganic.png', TRUE, 'chemistry-inorganic', 'Chemistry — Inorganic'),
-- (NOW(), NOW(), NULL, 'Study the extraction and purification of metals through metallurgy processes.', 'chemistry-metallurgy.png', TRUE, 'chemistry-metallurgy', 'Chemistry — Metallurgy'),
-- (NOW(), NOW(), NULL, 'Explore biomolecules like carbohydrates, proteins, lipids, and nucleic acids.', 'chemistry-biomolecules.png', TRUE, 'chemistry-biomolecules', 'Chemistry — Biomolecules');

-- INSERT INTO lessons_lesson 
-- (title, slug, order_index, course_id, created_at, updated_at, content_file)
-- VALUES
-- ('Introduction to Organic Chemistry', 'chemistry-organic-intro', 1, (SELECT id FROM courses_course WHERE slug='chemistry-organic'), NOW(), NOW(), 'chemistry-organic-intro.txt'),
-- ('Introduction to Physical Chemistry', 'chemistry-physical-intro', 1, (SELECT id FROM courses_course WHERE slug='chemistry-physical'), NOW(), NOW(), 'chemistry-physical-intro.txt'),
-- ('Introduction to Basic Concepts of Chemistry', 'chemistry-basicsconcepts-intro', 1, (SELECT id FROM courses_course WHERE slug='chemistry-basicsconcepts'), NOW(), NOW(), 'chemistry-basicsconcepts-intro.txt'),
-- ('Introduction to Inorganic Chemistry', 'chemistry-inorganic-intro', 1, (SELECT id FROM courses_course WHERE slug='chemistry-inorganic'), NOW(), NOW(), 'chemistry-inorganic-intro.txt'),
-- ('Introduction to Metallurgy', 'chemistry-metallurgy-intro', 1, (SELECT id FROM courses_course WHERE slug='chemistry-metallurgy'), NOW(), NOW(), 'chemistry-metallurgy-intro.txt'),
-- ('Introduction to Biomolecules', 'chemistry-biomolecules-intro', 1, (SELECT id FROM courses_course WHERE slug='chemistry-biomolecules'), NOW(), NOW(), 'chemistry-biomolecules-intro.txt');






-- INSERT INTO courses_course 
-- (created_at, updated_at, teacher_id, description, image, is_published, slug, title) 
-- VALUES
-- (NOW(), NOW(), NULL, 'Build a strong foundation in English grammar — tenses, verbs, and sentence structures.', 'english-grammar.png', TRUE, 'english-grammar', 'English — Grammar'),
-- (NOW(), NOW(), NULL, 'Enhance your vocabulary, learn new words, idioms, and their effective usage.', 'english-vocabulary.png', TRUE, 'english-vocabulary', 'English — Vocabulary'),
-- (NOW(), NOW(), NULL, 'Develop reading comprehension skills and interpret written passages with accuracy.', 'english-reading-comprehension.png', TRUE, 'english-reading-comprehension', 'English — Reading Comprehension'),
-- (NOW(), NOW(), NULL, 'Improve your writing — from essays to professional communication.', 'english-writing-skills.png', TRUE, 'english-writing-skills', 'English — Writing Skills'),
-- (NOW(), NOW(), NULL, 'Master spoken English and pronunciation for confident communication.', 'english-speaking.png', TRUE, 'english-speaking', 'English — Speaking & Pronunciation'),
-- (NOW(), NOW(), NULL, 'Explore English literature — poetry, prose, and classic works of great authors.', 'english-literature.png', TRUE, 'english-literature', 'English — Literature');

-- INSERT INTO lessons_lesson 
-- (title, slug, order_index, course_id, created_at, updated_at, content_file)
-- VALUES
-- ('Introduction to Grammar', 'english-grammar-intro', 60, (SELECT id FROM courses_course WHERE slug='english-grammar'), NOW(), NOW(), 'english-grammar-intro.txt'),
-- ('Introduction to Vocabulary', 'english-vocabulary-intro', 61, (SELECT id FROM courses_course WHERE slug='english-vocabulary'), NOW(), NOW(), 'english-vocabulary-intro.txt'),
-- ('Introduction to Reading Comprehension', 'english-reading-comprehension-intro', 62, (SELECT id FROM courses_course WHERE slug='english-reading-comprehension'), NOW(), NOW(), 'english-reading-comprehension-intro.txt'),
-- ('Introduction to Writing Skills', 'english-writing-skills-intro', 63, (SELECT id FROM courses_course WHERE slug='english-writing-skills'), NOW(), NOW(), 'english-writing-skills-intro.txt'),
-- ('Introduction to Speaking & Pronunciation', 'english-speaking-intro', 64, (SELECT id FROM courses_course WHERE slug='english-speaking'), NOW(), NOW(), 'english-speaking-intro.txt'),
-- ('Introduction to Literature', 'english-literature-intro', 65, (SELECT id FROM courses_course WHERE slug='english-literature'), NOW(), NOW(), 'english-literature-intro.txt');


-- Biology — Botany
-- Biology — Kingdoms
-- Biology — Microbiology
-- Biology — Physiology
-- Biology — Zoology

-- English — Grammar
-- English — Literature
-- English — Reading Comprehension
-- English — Speaking & Pronunciation
-- English — Vocabulary
-- English — Writing Skills

-- Mathematics — Algebra
-- Mathematics — Calculus
-- Mathematics — Geometry
-- Mathematics — Set & Relations
-- Mathematics — Statistics & Probabilities
-- Mathematics — Trigonometry

-- Physics — Atoms
-- Physics — Gravitation
-- Physics Kinematics
-- Physics — Magnetism
-- Physics — Optics
-- Physics — Thermodynamics




















