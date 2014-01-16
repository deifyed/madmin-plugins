import sys
from database import LoanManager

class Plugin():
    def __init__(self, ctx):
        self.context = context
        self.lm = LoanManager()

    def parse(self, data):
        # Help
        if data['cmd'] == '?':
            print('Commands:')
            print('     add     Adds a new debt')
            print('     list    Lists all debts')
            print('     clear   Clears debts')

        # Add new debt
        if data['cmd'] == 'add':
            if data['args'] == None or len(data['args']) < 3:
                print('add [person] [amount] [description]')
            else:
                args = data['args']
                self.lm.addDebt(args[0], args[1], args[2])

        # List either all debts or all debts to one person
        if data['cmd'] == 'list':
            if not data['args']:
                print('list [name], if no name is specified, lists all people')
                print('you owe money')
            elif data['args'] and len(data['args']) == 1:
                self.lm.listLoans(data['args'][0])
            else:
                self.lm.listLoans('all')

        # Clear debt
        if data['cmd'] == 'clear' and len(data['args']) == 2:
            self.lm.clearDebt(data['args'][0], data['args'][1])
        else:
            print('clear [person] [debt id]')
            print('debt id can be \'all\'')
            

if __name__ == '__main__':
    p = Plugin()

    data = dict()
    data['cmd'] = 'add'
    data['args'] = ['Børs', '200', 'pizza']
    p.parse(data)
