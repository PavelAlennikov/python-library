docker exec -i env-db-1 sh -c "exec mariadb -u root -p"pass"" < ./init_db.sql