docker-compose run db dropdb -h db -U postgres sense_db
docker-compose run db createdb -h db -U postgres sense_db
docker-compose run db psql -h db -U postgres -f /schema.sql sense_db