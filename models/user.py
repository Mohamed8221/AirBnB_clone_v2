#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the User class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

=======
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
>>>>>>> c7d022d9b2123cf8ce37c182e22546a591993c53

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
