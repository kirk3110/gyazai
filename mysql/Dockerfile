FROM mysql:5.7

COPY charset.cnf /etc/mysql/conf.d/charset.cnf
COPY prepare.sql /docker-entrypoint-initdb.d/prepare.sql
