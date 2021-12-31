# ORM 라이브러리 중 하나
# 관계형 데이터베이스RDBMS 에 엑세스하기 위한 레퍼같은 것
# 오브젝트 지향형으로 데이터베이스에 접근이 간단함

import sqlalchemy
from sqlalchemy import sql
import sqlalchemy.ext.declarative
import sqlalchemy.orm

engine = sqlalchemy.create_engine('sqlite:///:memory:')

Base = sqlalchemy.ext.declarative.declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    name = sqlalchemy.Column(sqlalchemy.String(14))

Base.metadata.create_all(engine)

# 데이터베이스에 엑세스하기 위해 세션을 만듬
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

person = Person(name = "Mike")
session.add(person)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)