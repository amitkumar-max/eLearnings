-- SELECT * FROM users_customuser;
-- ;
-- -- Add / Ensure new columns
-- ALTER TABLE users_customuser
--     ADD COLUMN IF NOT EXISTS full_name VARCHAR(255),
--     ADD COLUMN IF NOT EXISTS role VARCHAR(50) CHECK (role IN ('admin', 'teacher', 'student', 'moderator')),
--     ADD COLUMN IF NOT EXISTS address TEXT,
--     ADD COLUMN IF NOT EXISTS avatar VARCHAR(255),
--     ADD COLUMN IF NOT EXISTS banner VARCHAR(255),
--     ADD COLUMN IF NOT EXISTS bio TEXT,
--     ADD COLUMN IF NOT EXISTS date_of_birth DATE,
--     ADD COLUMN IF NOT EXISTS is_verified BOOLEAN DEFAULT FALSE,
--     ADD COLUMN IF NOT EXISTS phone_number VARCHAR(20),
--     ADD COLUMN IF NOT EXISTS created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- Ye sab tables show karega jo public schema me hain
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

