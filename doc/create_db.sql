CREATE DATABASE "Backend-2" ;

CREATE USER "Backend-2_user" WITH PASSWORD 'sajadfallahdoost1234' ;

ALTER ROLE "Backend-2_user" SET client_encoding TO 'utf8' ;

ALTER ROLE "Backend-2_user" SET default_transaction_isolation TO 'read committed' ;

ALTER ROLE "Backend-2_user" SET timezone TO 'UTC' ;

ALTER USER "Backend-2_user" CREATEDB ;

GRANT ALL PRIVILEGES ON DATABASE Backend-2 TO "Backend-2_user" ;

GRANT ALL ON schema public TO "Backend-2_user" ;

SELECT has_schema_privilege( 'Backend-2_user','public','CREATE') ;

ALTER DATABASE "Backend-2" OWNER TO "Backend-2_user" ;
