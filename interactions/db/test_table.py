# -*- coding = utf-8 -*-

from flask import flash

from interactions.init import db


class SummaryTable(db.Model):

    __tablename__ = "Summary_Table"
    id = db.Column(db.Integer, primary_key=True)
    table_name = db.Column(db.String)
    id_start = db.Column(db.Integer)
    id_end = db.Column(db.Integer)



def create_table(table_name: str):

    class Table(db.Model):

        __tablename__ = str(table_name)
        id = db.Column(db.Integer, primary_key=True)
        field_1 = db.Column(db.String, default="test")
        field_2 = db.Column(db.String, default="test")
        field_3 = db.Column(db.String, default="test")
        field_4 = db.Column(db.String, default="test")
        field_5 = db.Column(db.String, default="test")
        field_6 = db.Column(db.String, default="test")
        field_7 = db.Column(db.String, default="test")
        field_8 = db.Column(db.String, default="test")
        field_9 = db.Column(db.String, default="test")

        def __repr__(self):
            return 'Table:%s,%s' % self.id

        @staticmethod
        def add(data: dict):
            """
            添加数据
            :param data:
            :return:
            """
            if isinstance(data, list):
                for _data in data:
                    db.session.add(Table(field_1=_data["data"]))
            else:
                db.session.add(Table(field_1=data["data"]))
            db.session.commit()

        @staticmethod
        def delete(_id):
            """
            delete by id
            :return:
            """
            if isinstance(_id, int) or isinstance(_id, str):
                data = [Table.query.get(_id)]
            elif isinstance(_id, list):
                data = [Table.query.get(__id) for __id in _id]
            else:
                data = []

            if data:
                try:
                    for _data in data:
                        db.session.delete(data)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    flash('操作失败')
                    db.session.rollback()
            else:
                flash('数据不存在')

    return Table


if __name__ == '__main__':
    pass