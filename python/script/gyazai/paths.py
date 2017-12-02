# -*- coding: utf-8 -*-

import os.path


class DirPaths:
    '''
    プロジェクト内のディレクトリパスを定義
    '''
    MODULE_DIR = os.path.abspath(os.path.join(__file__, '..'))
    SCRIPT_DIR = os.path.abspath(os.path.join(MODULE_DIR, '..'))
    PYTHON_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
    LOGS_DIR = os.path.abspath(os.path.join(PYTHON_DIR, 'logs'))
    DATA_DIR = os.path.abspath(os.path.join(PYTHON_DIR, 'data'))


class DataFilePaths:
    '''
    データファイル（テキスト）パスを定義
    '''
    ENG_TEXT = os.path.abspath(os.path.join(DirPaths.DATA_DIR, 'eng_text.csv'))
    JAN_TEXT = os.path.abspath(os.path.join(DirPaths.DATA_DIR, 'jan_text.csv'))
