#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:@localhost/sqlalchemy_lab?charset=utf8', encoding='utf8', echo=True)
DBSession = sessionmaker(bind=engine)


def main():
    session = DBSession()
    session.excute("update tag set group_id = group_id+1 where id = 7 ")
    session.commit()


if __name__ == '__main__':
    main()