import sqlite3
from database import LoanManager

class Loan():
    def __init__(self, person, amount, description):
        self.person = person
        self.description = description
        self.amount = amount

    def save(self):
        lm = LoanManager()

        lm.save(self)
