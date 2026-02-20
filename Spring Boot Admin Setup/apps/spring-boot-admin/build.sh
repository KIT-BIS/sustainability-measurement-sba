#!/bin/sh
docker compose down -v
docker build --tag spring-boot-admin-nginx .
