# -*- coding: utf-8 -*-

import re
import urllib.request
from collections import defaultdict
from bs4 import BeautifulSoup

from carddata import CardData


class CardDataCollecter:
    @classmethod
    def collect_all_card_data(class_):
        for card_name in class_.collect_all_card_names():
            yield class_.extract_card_data_from_wg(card_name)
            break
            sleep(300)

    CARD_NAMES_SOURCE_URL = 'http://whisper.wisdom-guild.net/search.php?name=&name_ope=and&mcost=&mcost_op=able&mcost_x=may&ccost_more=0&ccost_less=&msw_gt=0&msw_lt=&msu_gt=0&msu_lt=&msb_gt=0&msb_lt=&ms_ope=and&msr_gt=0&msr_lt=&msg_gt=0&msg_lt=&msc_gt=0&msc_lt=&msp_gt=0&msp_lt=&msh_gt=0&msh_lt=&color_multi=able&color_ope=and&rarity_ope=or&text=&text_ope=and&oracle=&oracle_ope=and&p_more=&p_less=&t_more=&t_less=&l_more=&l_less=&display=cardname&supertype_ope=or&cardtype_ope=or&subtype_ope=or&format=all&exclude=no&set_ope=or&illus_ope=or&illus_ope=or&flavor=&flavor_ope=and&sort=name_en&sort_op=&output=text'
    CARD_NAME_HEADER = '　英語名：'

    @classmethod
    def collect_all_card_names(class_):
        with urllib.request.urlopen(class_.CARD_NAMES_SOURCE_URL) as response:
            lines = (line.decode('shift-jis').rstrip()
                     for line in response.readlines())
            for line in lines:
                if line[:5] == class_.CARD_NAME_HEADER:
                    yield line[5:]

    WG_ROOT_URL = 'http://whisper.wisdom-guild.net/card/'

    @classmethod
    def extract_card_data_from_wg(class_, card_name):
        card_data_url = class_.WG_ROOT_URL + urllib.parse.quote(card_name)
        with urllib.request.urlopen(card_data_url) as responce:
            html = responce.read()
            soup = BeautifulSoup(html, 'lxml')
            card_div = soup.find('div', class_='wg-whisper-card-detail')
            first_row_class = card_div.table.tr.get('class')
            rows = card_div.find_all('tr', class_=first_row_class)
            th_td_dict = defaultdict(
                str, {row.th.text: row.td.text for row in rows})

            card_data = CardData()
            name = th_td_dict['カード名']
            card_data.jan_name, card_data.eng_name \
                = class_._split_name_to_eng_and_jan(class_, name)
            card_data.mana_cost = th_td_dict['マナコスト']
            card_data.type_ = th_td_dict['タイプ'].replace('\n', '')
            card_data.jan_text = th_td_dict['テキスト']
            card_data.eng_text = th_td_dict['オラクル']
            card_data.power_toughness = th_td_dict['Ｐ／Ｔ']
            card_data.loyality = th_td_dict['忠誠度']

            return card_data

    RE_NEEDLESS = re.compile(r'\n+|\t|（.*）')

    def _split_name_to_eng_and_jan(self, name):
        name = self.RE_NEEDLESS.sub('', name)
        names = name.split('/')
        if len(names) > 1:
            return names
        elif len(names) == 1:
            return (names[0], names[0])
        else:
            return('', '')


if __name__ == '__main__':
    collecter = CardDataCollecter()
    all_card_data = collecter.collect_all_card_data()
    for card_data in all_card_data:
        print(card_data)
