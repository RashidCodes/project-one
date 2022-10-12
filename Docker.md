--in postgres, clear existing tables
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

#from one folder level above src/
docker build . -t crypto
docker run --rm --env-file=.env crypto
