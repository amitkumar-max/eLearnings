-- SELECT * FROM django_migrations;
-- SQLTools me run
-- INSERT INTO django_migrations (app, name, applied)
-- VALUES ('users','0001_initial', now());




-- SELECT * FROM django_migrations;



-- \dt users*

SELECT tablename 
FROM pg_tables 
WHERE schemaname = 'public' AND tablename LIKE 'users%';



















