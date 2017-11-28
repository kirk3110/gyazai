#!/bin/sh
cd $(dirname $0)
docker-compose exec -d python python script/gyazai/collect_card_data_main.py
