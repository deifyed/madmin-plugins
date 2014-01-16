#import sqlite3

class DebtManager():
    def __init__(self, connection):
        self.connection = connection
        self.connection.execute('''
            create table if not exists debt(
                    _id integer primary key,
                    pid integer references person(_id),
                    amount integer not null,
                    desc text);''')
    def close(self):
        self.connection.close()

    # Adding debt to database
    def append(self, personid, amount, description):
        result = self.connection.execute('''
            insert into debt(pid, amount, desc)
            values ({pid},{a},\'{d}\');'''.format(pid=personid,
                                                  a=amount,
                                                  d=description))

        if(result.lastrowid):
            self.connection.commit()

            return(result.lastrowid)
        else:
            return(None)

    def getTotalAmount(self, pid):
        result = self.connection.execute('''
            select sum(amount)
            from debt
            where pid={i};'''.format(i=pid))

        return(result.fetchone()[0])

    def clearAllDebt(self, pid):
        result = self.connection.execute('''
            delete from debt
            where pid={p}'''.format(p=pid))

        self.connection.commit()

    def clearDebt(self, debtid, personid):
        result = self.connection.execute('''
            delete from debt
            where _id={did}
            and pid={pid}'''.format(did=debtid,
                                    pid=personid))

        self.connection.commit()

    # Retrieving debt from table
    def __getitem__(self, pid):
        result = self.connection.execute('''
            select _id,amount,desc
            from debt
            where pid={i};'''.format(i=pid))

        if(result):
            return(result)
        else:
            return(None)

    # Updating person from table person
    def __setitem__(self, index, value):
        
        result = self.connection.execute('''
            update person
            set name=\'{v}\'
            where _id={i};'''.format(v=value, i=index))

        self.connection.commit()
