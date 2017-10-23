# -*- coding: utf-8 -*-
import sys
import os.path
import logging
import logging.handlers

from collecter import CardDataCollecter
from db import GyazaiDB
from paths import DirPaths


def main():
    # ログ設定
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 標準出力へのハンドラ
    stdout_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stdout_handler)
    # ログファイルへのハンドラ
    log_file_path = os.path.join(DirPaths.LOGS_DIR, 'collect_card_data.log')
    file_handler = logging.handlers.RotatingFileHandler(log_file_path,
                                                        maxBytes=1048576)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s: %(levelname)s: %(message)s"))
    logger.addHandler(file_handler)

    try:
        logger.info('Start collecting card data')
        # DBに接続
        with GyazaiDB.connect(host='mysql',
                              user='gyazai_user',
                              password='gyazai_user_password') as gyazai_db:
            # 全てのカード情報をデータベースに登録
            for i, card_data in enumerate(
              CardDataCollecter.collect_all_card_data()):
                gyazai_db.insert_card_data(card_data)
                logger.info('Insert row %d: %s (%s)',
                            i+1, card_data.eng_name, card_data.jan_name)
    except Exception as e:
        logger.exception(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
