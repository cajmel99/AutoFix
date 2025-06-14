bash start_postgres.sh

docker build -t autofix-backend .
docker run -d --name autofix-backend -p 8000:8000 --network autofix_network autofix-backend
