#!/bin/bash

CONTAINER_NAME=autofix_postgres

DB_NAME=autofix
DB_USER=autofix_user
DB_PASSWORD=autofix_pass
DB_PORT=5434
NETWORK_NAME=autofix_network

if [ -z "$(docker network ls --filter name=^${NETWORK_NAME}$ --format='{{.Name}}')" ]; then
    docker network create $NETWORK_NAME
fi

if [ "$(docker ps -a -q -f name=$CONTAINER_NAME)" ]; then
    docker start $CONTAINER_NAME
else
    docker run -d \
        --name $CONTAINER_NAME \
        --network $NETWORK_NAME \
        -e POSTGRES_DB=$DB_NAME \
        -e POSTGRES_USER=$DB_USER \
        -e POSTGRES_PASSWORD=$DB_PASSWORD \
        -p $DB_PORT:5432 \
        postgres:15
fi
