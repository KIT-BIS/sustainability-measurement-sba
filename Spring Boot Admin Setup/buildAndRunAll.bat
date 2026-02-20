@echo off

cd apps\spring-boot-admin
call build.bat
cd ..\..

cd apps\hello-world
call build.bat
cd ..\..

docker compose up -d
