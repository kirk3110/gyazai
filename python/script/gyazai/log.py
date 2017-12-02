# -*- coding: utf-8 -*-
import sys
import os.path
import logging
import logging.handlers

from paths import DirPaths


def setup_logger(log_file_name):
    # ログ設定
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 標準出力へのハンドラ
    stdout_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stdout_handler)
    # ログファイルへのハンドラ
    log_file_path = os.path.join(DirPaths.LOGS_DIR, log_file_name)
    file_handler = logging.handlers.RotatingFileHandler(log_file_path,
                                                        maxBytes=1048576)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s: %(levelname)s: %(message)s"))
    logger.addHandler(file_handler)

    return logger
