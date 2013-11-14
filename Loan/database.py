import sqlite3

from config import *
from Loan import Loan

table_loans = {
    'name':'loans',
    'create':'create table if not exists loans(_id integer primary key,\
                                               person text not null,\
                                               description text,\
                                               amount integer not null);',
    'key_id':'_id',
    'key_person':'person',
    'key_description':'desc',
    'key_amount':'amount'
}

class LoanManager():
    def __init__(self):
        self.connection = sqlite3.connect(DB_PATH)
        self.connection.execute(table_loans['create'])

    def close(self):
        self.connection.close()

    def save(self, loan):
        self.connection.execute('insert into {table}({keys}) values(\
        \'{person}\',\'{description}\',{amount});'.format(table=table_loans['name'],
                                                          keys=table_loans['key_person'] + ',' +
                                                               table_loans['key_description'] + ',' +
                                                               table_loans['key_amount'],
                                                          person=loan.person,
                                                          description=loan.description,
                                                          amount=loan.amount))
