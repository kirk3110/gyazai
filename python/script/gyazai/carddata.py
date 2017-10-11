# -*- coding: utf-8 -*-

from collections import defaultdict


class CardData:
    '''
    カードデータクラス
    '''
    # 要素はここで挙げておく
    # カードデータ用DB（card_data）のフィールドと要素が一致するようにする
    ATTRIBUTES = ['jan_name',         # 日本語名
                  'eng_name',         # 英語名
                  'jan_text',         # 日本語テキスト
                  'eng_text',         # 英語テキスト
                  'type_',            # カードタイプ
                  'power_toughness',  # P/T
                  'mana_cost',        # マナコスト
                  'loyality']         # 忠誠度

    def __init__(self, dict_=None, **kwargs):
        '''
        コンストラクタ
        '''
        # dictが入力された場合はそこから要素を探す
        if dict_:
            dict_ = defaultdict(str, dict_)
        # 可変長引数で各要素の文字列が渡された場合はそれらを用いる
        else:
            dict_ = defaultdict(str, kwargs)
        for attribute in self.ATTRIBUTES:
            self.__setattr__(attribute, dict_[attribute])

    def __repr__(self):
        # print()された場合は、要素の順番を維持した上でdictライクに表示される
        return '{' + ', '.join(
            ['{0}: {1}'.format(attribute,
                               repr(self.__getattribute__(attribute)))
             for attribute in self.ATTRIBUTES]) + '}'
