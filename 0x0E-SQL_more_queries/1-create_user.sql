-- Creates the MySQL server user `user_0d_1` with password `user_0d_1_pwd`
-- and all privileges granted
CREATE USER IF NOT EXISTS user_0d_1@localhost;

/* Set password for user `user_0d_1` */
SET PASSWORD FOR user_0d_1@localhost = 'user_0d_1_pwd';

/* Grant user `user_0d_1` all privileges on the MySQL Server */
GRANT ALL PRIVILEGES
	ON *.*
	TO user_0d_1@localhost;

