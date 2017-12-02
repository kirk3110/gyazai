# -*- coding: utf-8 -*-
import sys
import csv

from log import setup_logger
from db import GyazaiDB
from paths import DirPaths, DataFilePaths
from normalizer import EngTextNormalizer


def main():
    logger = setup_logger('normalize_card_text.log')

    try:
        logger.info('Start normalizing card text')
        # DBに接続
        with GyazaiDB.connect(host='mysql',
                              user='gyazai_user',
                              password='gyazai_user_password') as gyazai_db:
            # 全てのカード情報から英語名だけを先に取得
            all_eng_names = [card_data.eng_name
                             for card_data in gyazai_db.fetch_all_card_data()]
            card_data_length = len(all_eng_names)
            normalizer = EngTextNormalizer(all_eng_names)    # 正規化フィルタ
            # CSVファイルに書き出し
            with open(DataFilePaths.ENG_TEXT, 'w') as f:
                writer = csv.writer(f, lineterminator='\n')
                for i, card_data in enumerate(gyazai_db.fetch_all_card_data()):
                    # 1つずつ英語テキストを正規化する
                    writer.writerow([card_data.jan_name,
                                     normalizer.normalize(card_data.eng_name,
                                                          card_data.eng_text)])
                    logger.info('Normalize %d/%d: %s',
                                i+1, card_data_length, card_data.jan_name)
    except Exception as e:
        logger.exception(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
