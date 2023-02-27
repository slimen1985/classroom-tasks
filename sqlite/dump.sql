BEGIN TRANSACTION;
CREATE TABLE users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            FNAME CHAR(20) NOT NULL,
            lname CHAR(20) NOT NULL);
INSERT INTO "users" VALUES(1,'John','Lock');
INSERT INTO "users" VALUES(2,'Jack','Shepard');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('users',2);
COMMIT;
