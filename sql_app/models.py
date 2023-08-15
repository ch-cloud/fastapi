from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, MetaData
from .database import Base, engine
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)  # 设置主键和索引
    email = Column(String(32), unique=True, index=True)
    hashed_password = Column(String(32))
    is_active = Column(Boolean, default=True)
    items = relationship('Item', back_populates='owner')


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(32), index=True)
    description = Column(String(32), index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='items')

