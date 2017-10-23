# -*- coding: utf-8 -*-
import re


class EngTextNormalizer:
    '''
    英語テキストの正規化を行うクラス
    '''
    RE_MANA = re.compile(
        r'({(W|U|B|R|G|C|S|[0-9]+|T|Q|X|½|∞)/?(W|U|B|R|G|C|S|P|[0-9]+|T|Q|X|½|∞)?})+')
    RE_NUM = re.compile(r'([0-9]+|½| X )')
    RE_MARK = re.compile(r'(,|\.|:|;|—|\(|\)|\"|/|\+|-|\!|\?|\u3000|\'s|\n)')
    RE_SPACES = re.compile(r' +')

    MANA_TAG = '<mana>'
    NUM_TAG = '<num>'
    MYSELF_TAG = '<myself>'

    def __init__(self, all_names):
        self.all_names = all_names
        # カード名のタグ付けに用いる
        self._name_tags = ((self._minimum_normalize(name),
                            self._minimum_normalize(name).replace(' ', '_'))
                           for name in self.all_names)

    def normalize(self, this_name, text):
        # そのカード自身の名前・マナシンボル・数値はそれぞれタグに置き換えられる
        text = text.replace(this_name, self.MYSELF_TAG)
        text = self.RE_MANA.sub(self.MANA_TAG, text)
        text = self.RE_NUM.sub(self.NUM_TAG, text)
        # 他のカードの名前はスペースで繋げられる
        for raw_name, name_tag in self._name_tags:
            text = text.replace(raw_name, name_tag)
        # 残りの部分も正規化
        text = self._minimum_normalize(text)
        return text

    def _minimum_normalize(self, str_):
        # 記号はスペースに置き換えられる
        str_ = self.RE_MARK.sub(' ', str_)
        # 複数スペースを詰める
        str_ = self.RE_SPACES.sub(' ', str_)
        # 小文字に揃える
        return str_.lower()
