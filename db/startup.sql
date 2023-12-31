REASSIGN OWNED BY blogdev TO postgres;
DROP OWNED BY blogdev;
DROP USER IF EXISTS blogdev;
DROP DATABASE IF EXISTS blogdb;
CREATE USER blog_dev WITH ENCRYPTED PASSWORD 'blog_dev_pwd' CREATEDB CREATEROLE;
CREATE DATABASE blog_db
	TEMPLATE template0
	OWNER blog_dev
	ENCODING 'utf8'
	LC_COLLATE 'en_US.utf8'
	LC_CTYPE 'en_US.utf8';

ALTER SCHEMA public OWNER to postgres;
GRANT ALL PRIVILEGES ON DATABASE blog_db to blog_dev;
GRANT USAGE, CREATE ON SCHEMA public TO blog_dev;
