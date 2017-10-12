# -*- coding: utf-8 -*-
from tqdm import tqdm

from collecter import CardDataCollecter
from db import GyazaiDB

if __name__ == '__main__':
    # DBに接続
    with GyazaiDB.connect(host='mysql',
                          user='gyazai_user',
                          password='gyazai_user_password') as gyazai_db:
        # 全てのカード情報をデータベースに登録
        for card_data in tqdm(CardDataCollecter.collect_all_card_data()):
            gyazai_db.insert_card_data(card_data)
