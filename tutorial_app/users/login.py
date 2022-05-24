import hashlib

from django.db import connection

def login_func(username, password):
    stmt2 = "SELECT username, password FROM db_manager"
    cursor = connection.cursor()
    cursor.execute(stmt2)
    connection.commit()
    dbmanagers = cursor.fetchall()

    hasher = hashlib.sha256()
    newpw = hasher.hexdigest()
    password = newpw

    for dbm in dbmanagers:
        if username == dbm[0] and password == dbm[1]:
            return "manager"

    stmt = "SELECT user_name, password FROM user"
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    users = cursor.fetchall()

    for u in users:
        if username == u[0] and password == u[1]:
            return "user"
    return "fail"