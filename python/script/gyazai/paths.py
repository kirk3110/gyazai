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
