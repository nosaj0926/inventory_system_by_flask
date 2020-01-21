# -*- coding: utf-8 -*-
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from ..setting import Base
from ..setting import ENGINE
from ..setting import session

class Item(Base):
    """
    商品モデル
    """
    __tablename__ = 'item'
    id = Column('id', String(10), primary_key = True)
    name = Column('name', String(50))
    amount = Column('amount', Integer)

    def __str__(self):
        return '{"id": "%s", "name": "%s", "amount": "%s"}' % (self.id, self.name, self.amount)