from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class ExpensesService:

    def __init__(self, exp_repo):
        self.exp_repo = exp_repo





