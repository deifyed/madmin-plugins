import sqlite3

from personmanager import PersonManager
from debtmanager import DebtManager

DB_NAME = 'debtdb'

class LoanManager():
    
    def __init__(self):
        connection = sqlite3.connect(DB_NAME)

        self.persons = PersonManager(connection)
        self.debt = DebtManager(connection)

    def addDebt(self, person, amount, description):
        pid = self.persons.findPerson(person)

        if pid == None:
            pid = self.persons.append(person)

        self.debt.append(pid, amount, description)

    def listLoans(self, target):
        if target == 'all':
            persons = self.persons.getAllPersons()

            for pid, name in persons:
                amount = self.debt.getTotalAmount(pid)

                print(name + ': ' + str(amount) + 'kr')
        else:
            pid = self.persons.findPerson(target)

            for did, amount, desc in self.debt[pid]:
                print(str(did) + ':' + str(amount) + ' ' + desc)

    def clearDebt(self, person, debt):
        pid = self.persons.findPerson(person)

        if debt == 'all' and pid:
            self.debt.clearAllDebt(pid)
            del self.persons[pid]
        else:
            self.debt.clearDebt(debt, pid)

if __name__ == '__main__':
    db = Database()

    db.addDebt('Bear', 300, 'pizza')
