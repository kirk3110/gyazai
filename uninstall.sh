#!/bin/sh
cd $(dirname $0)
docker-compose down
docker rmi gyazai_python
docker rmi gyazai_mysql
