from django.db import connection


def returnAll():
        stmt = "SELECT * FROM user"
        cursor = connection.cursor()
        cursor.execute(stmt)
        connection.commit()
        tmp = cursor.fetchall()
        print(tmp)
        elms = []
        for s in tmp:
            x = {"username": s[0], "institute": s[1], "password": s[2]}
            elms.append(x)
        return elms