from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    score = Column(Integer())
    age = Column(Integer())


class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))


engine = create_engine('sqlite:///./test.db', echo=True)

Base.metadata.bind = engine
#Base.metadata.drop_all()
Base.metadata.create_all()
# Base.metadata.clear()


# DBSession = sessionmaker(bind=engine)
#
# session = DBSession()
# new_user = User(id='209', name='Bob')
# session.add(new_user)
# session.commit()
# session.close()
#
# session = DBSession()
# users = session.query(User).filter(User.id > '1').all()
# for u in users:
#     print(u.id, u.name)
#
# session.close()
