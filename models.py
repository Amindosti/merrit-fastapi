from database import Base
from sqlalchemy import Integer, String, Column


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    role = Column(String)


class NewForm(Base):
    __tablename__ = 'form'
    form_id = Column(Integer, primary_key=True, index=True)
    author = Column(String)
    Form = Column(String)
    Form_name = Column(String)
    Privacy = Column(String)


class DataEntry(Base):
    __tablename__ = 'dataentry'
    form_id1 = Column(Integer, primary_key=True, index=True)
    writer = Column(String)
    formId = Column(String)
    answer = Column(String)
