from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


association_table = Table(
    'association_table', Base.metadata,     
    Column('user_id', ForeignKey('user.id', ondelete="CASCADE"), primary_key=True),
    Column('book_id', ForeignKey('book.id', ondelete="CASCADE"), primary_key=True)
)

class User(Base):
    __tablename__ = "user"
    id       = Column(Integer,      primary_key=True)
    email    = Column(String(100),  nullable=False, unique=True)
    password = Column(String(100),  nullable=False)
    books    = relationship("Book", secondary=association_table)


class Book(Base):
    __tablename__ = "book"
    id     = Column(Integer,     primary_key=True)
    title  = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    price  = Column(Float,       nullable=False)
