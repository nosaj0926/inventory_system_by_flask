# -*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

# DBの設定
DATABASE = 'postgres://ylbllyzjwtkkmb:defbbc4afe7c99f199fe6d674052ede00261e54d80e7ce1fcd6a861d1bea79d7@ec2-34-197-171-33.compute-1.amazonaws.com:5432/d1kcem5p95frod'
ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit = False, # 自動コミット
        autoflush = True, # 自動反映
        bind = ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()