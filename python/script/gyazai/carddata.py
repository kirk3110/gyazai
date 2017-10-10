# -*- coding: utf-8 -*-

from collections import defaultdict


class CardData:
    ATTRIBUTES = ['jan_name', 'eng_name', 'jan_text', 'eng_text',
                  'type_', 'power_toughness', 'mana_cost', 'loyality']

    def __init__(self, dict_=None, **kwargs):
        if dict_:
            dict_ = defaultdict(str, dict_)
        else:
            dict_ = defaultdict(str, kwargs)
        for attribute in self.ATTRIBUTES:
            self.__setattr__(attribute, dict_[attribute])

    def __repr__(self):
        return '{' + ', '.join(
            ['{0}: {1}'.format(attribute,
                               repr(self.__getattribute__(attribute)))
             for attribute in self.ATTRIBUTES]) + '}'
