# -*- coding: utf-8 -*-

from contextlib import contextmanager
import pymysql.cursors

from carddata import CardData


class GyazaiDB:
    '''
    gyazai専用データベースのインタフェースクラス
    '''
    @staticmethod
    @contextmanager
    def connect(host, user, password):
        '''
        カードデータ用DBへの接続を行う
        '''
        gyazai_db = GyazaiDB()
        # DBに接続する
        gyazai_db.connection = pymysql.connect(
            host=host, user=user, password=password,
            db='gyazai', charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)
        gyazai_db.cursor = gyazai_db.connection.cursor()
        try:
            yield gyazai_db
        # 自動的にクローズする
        finally:
            gyazai_db.disconnect()

    def disconnect(self):
        '''
        DBとの接続を遮断する
        '''
        self.cursor.close()
        self.connection.close()

    def insert_card_data(self, card_data):
        '''
        1件ぶんのカードデータをカードデータDBに追加する
        '''
        sql = 'INSERT INTO \
card_data(jan_name, eng_name, jan_text, eng_text, \
type_, power_toughness, mana_cost, loyality) \
VALUES(%s, %s, %s, %s, %s, %s, %s, %s);'
        self.cursor.execute(sql, (
            card_data.jan_name, card_data.eng_name,
            card_data.jan_text, card_data.eng_text,
            card_data.type_, card_data.power_toughness,
            card_data.mana_cost, card_data.loyality))
        self.connection.commit()

    def fetch_all_card_data(self, **kwargs):
        '''
        DBに登録されている全てのカード情報を取得する
        '''
        # 全てのカード情報を取得
        self.cursor.execute('SELECT * FROM card_data;')
        # CardData形式に詰め替え
        for row in self.cursor.fetchall():
            yield CardData(
                jan_name=row['jan_name'], eng_name=row['eng_name'],
                jan_text=row['jan_text'], eng_text=row['eng_text'],
                type_=row['type'], power_toughness=row['power_toughness'],
                mana_cost=row['mana_cost'], loyality=row['loyality'])
