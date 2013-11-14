import sqlite3
import Loan

class Plugin():
    def __init__(self):
        pass

    def parse(self, data):
        if data['cmd'] == 'add':
            if data['args'] == None or len(data['args']) < 3:
                print('add [person] [amount] [description]')
            else:
                args = data['args']
                l = Loan(args[0], args[1], args[2])
                l.save()
