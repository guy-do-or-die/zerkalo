CREATE SEQUENCE user_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1;
CREATE TABLE "user" (id integer NOT NULL DEFAULT nextval('user_id_seq'), email text NOT NULL, is_admin boolean);
ALTER TABLE ONLY "user" ADD CONSTRAINT user_pkey PRIMARY KEY (id);

CREATE SEQUENCE role_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1;
CREATE TABLE role (id integer NOT NULL DEFAULT nextval('role_id_seq'), name text NOT NULL, permissions text);
ALTER TABLE ONLY role ADD CONSTRAINT role_pkey PRIMARY KEY (id);

CREATE TABLE roles_users (user_id integer, role_id integer);
ALTER TABLE ONLY roles_users ADD CONSTRAINT roles_users_role_id_fkey FOREIGN KEY (role_id) REFERENCES role(id);
ALTER TABLE ONLY roles_users ADD CONSTRAINT roles_users_user_id_fkey FOREIGN KEY (user_id) REFERENCES "user"(id);


CREATE SEQUENCE movie_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1;
CREATE TABLE movie (id integer NOT NULL DEFAULT nextval('movie_id_seq'), name text NOT NULL, user_id integer, description text, url text, rate integer, status integer, pic text);
ALTER TABLE ONLY movie ADD CONSTRAINT movie_pkey PRIMARY KEY (id);


CREATE SEQUENCE vote_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1;
CREATE TABLE vote (id integer NOT NULL DEFAULT nextval('vote_id_seq'), date timestamp without time zone DEFAULT now() NOT NULL, movie_id integer, user_id integer, weight integer);
ALTER TABLE ONLY vote ADD CONSTRAINT vote_pkey PRIMARY KEY (id);
