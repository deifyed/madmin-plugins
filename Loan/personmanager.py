import sqlite3

class PersonManager():
    def __init__(self, connection):
        self.connection = connection
        self.connection.execute('''
            create table if not exists person(
                    _id integer primary key,
                    name text not null);''')
    def close(self):
        self.connection.close()

    # Adding person to database
    def append(self, name):
        result = self.connection.execute('''
            insert into person(name)
            values (\'{n}\');'''.format(n=name))

        if(result.lastrowid):
            self.connection.commit()

            return(result.lastrowid)
        else:
            return(None)

    # Retrieve person by name
    def findPerson(self, name):
        result = self.connection.execute('''
            select _id
            from person
            where name=\'{n}\';'''.format(n=name))

        result = result.fetchone()

        if result:
            return(result[0])
        else:
            return None

    def getAllPersons(self):
        result = self.connection.execute('''
            select _id, name
            from person''')

        persons = list()

        for pid,name in result:
            persons.append((pid,name))

        return(persons)

    # Deleting person from table person
    def __delitem__(self, index):
        self.connection.execute('''
            delete from person
            where _id={i};'''.format(i=index))

        self.connection.commit()
