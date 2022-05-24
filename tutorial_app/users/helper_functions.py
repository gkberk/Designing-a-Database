from django.db import connection
import hashlib

def add_a_user(namex, username, institution, password): #2
    hasher = hashlib.sha256()
    newpw = hasher.hexdigest()
    password = newpw
   # stmt = "INSERT INTO user (name, user_name, institution, password"
    stmt = "INSERT INTO "
    stmt += "user (name, user_name, institution, password) VALUES("
    stmt += "'" + str(namex) + "', '" + str(username) + "', '" + str(institution) + "', '" + str(password) + "')"
 #   stmt = "INSERT INTO user (name, user_name, institution, password) VALUES("+namex+", "+username+", "+institution+", "+password+");"
    cursor = connection.cursor()
    cursor.execute(stmt)


def drug_info(drugid):  # unnecessary
    stmt = "SELECT * FROM drug WHERE drugID =" + drugid
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    druginfo = cursor.fetchall()
    return druginfo


def get_delete_drug(drugid): # 3.1
    stmt = "DELETE FROM drug WHERE drugID like '"+drugid+"'"
    cursor = connection.cursor()
    cursor.execute(stmt)


def get_update_affinity(reactionid, affinity):  # 3.2
    stmt = "UPDATE reaction"
    stmt += " SET affinity=" + affinity + " "
    stmt += "WHERE reactionID=" + reactionid

    cursor = connection.cursor()
    cursor.execute(stmt)


def get_delete_protein(proteinid): # 4
    stmt = "DELETE FROM protein WHERE proteinID like '"+proteinid+"'"
    cursor = connection.cursor()
    cursor.execute(stmt)

## 5!!!!

def get_drugs():  # 6.1
    stmt = "SELECT drugID, drug_name FROM drug"
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    drugs = cursor.fetchall()
    return drugs

def get_proteins(): # 6.2
    stmt = "SELECT proteinID FROM protein"
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    x = cursor.fetchall()
    return x
def get_sides(): # 6.3
    stmt = "SELECT umls_cui, side_name FROM sideeffects"
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    x = cursor.fetchall()
    return x
def get_interactions(): # 6.4
    stmt = "SELECT drug1ID, drug2ID FROM interaction"
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    x = cursor.fetchall()
    intr = []
    for i in x:
        intr.append((i[0],i[1]))
    return intr
def get_papers(): # 6.5
    stmt = "SELECT doi FROM foundby"
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    x = cursor.fetchall()
    return x
def get_users(): # 6.6
    stmt = "SELECT user_name FROM user"
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    x = cursor.fetchall()
    return x

def get_user_views(): #8
    stmt = "SELECT D.drugID, D.drug_name, D.SMILES, D.description, P.targetname, S.side_name "
    stmt += "FROM protein P INNER JOIN proteinreaction R on P.proteinID = "
    stmt += "R.proteinID INNER JOIN partof O on R.reactionID = O.reactionID "
    stmt += "INNER JOIN drug D on O.drugID=D.drugID INNER JOIN causes C on D.drugID= "
    stmt += "C.drugID INNER JOIN sideeffects S on C.umls_cui=S.umls_cui; "
  #  stmt = "SELECT * from drug D"
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    userview = cursor.fetchall()
    return userview



def drug_helper1(drugid): #9.1
    stmt = "SELECT D2.drugID, D2.drug_name "
    stmt += "FROM (SELECT I.drug2ID FROM drug D INNER JOIN interaction I on D.drugID=I.drug1ID "
    stmt += "WHERE D.drugID='" + drugid + "') "
    stmt += "AS Temp INNER JOIN drug D2 on D2.drugID=Temp.drug2ID "
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    drug1result = cursor.fetchall()
    return drug1result

def drug_helper2(drugid): #10
    stmt = "SELECT S.side_name, S.umls_cui "
    stmt += "FROM drug D INNER JOIN causes C on D.drugID=C.drugID INNER JOIN "
    stmt += "sideeffects S on C.umls_cui=S.umls_cui "
    stmt += "WHERE D.drugID like '" + drugid + "'"
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    drug2result = cursor.fetchall()
    return drug2result

def drug_helper3(drugid): #11
    stmt = "SELECT P.proteinID, P.targetname "
    stmt += "FROM drug D INNER JOIN partof O on D.drugID=O.drugID INNER JOIN "
    stmt += "reaction R on O.reactionID=R.reactionID INNER JOIN "
    stmt += "proteinreaction N on R.reactionID=N.reactionID INNER JOIN "
    stmt += "protein P on N.proteinID=P.proteinID "
    stmt += "WHERE D.drugID like '" + drugid + "'"
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    drug3result = cursor.fetchall()
    return drug3result

def get_interacting_drugs_of_protein(proteinid): #12
    stmt = "SELECT D.drugID, D.drug_name "
    stmt += "FROM drug D INNER JOIN partof O on D.drugID=O.drugID "
    stmt += "INNER JOIN reaction R on O.reactionID=R.reactionID INNER JOIN "
    stmt += "proteinreaction N on R.reactionID=N.reactionID INNER JOIN "
    stmt += "protein P on N.proteinID=P.proteinID "
    stmt += "WHERE P.proteinID = '" + proteinid + "'"

    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    result = cursor.fetchall()
    return result

def get_drugs_affecting_same_protein(): #13
    stmt = "SELECT proteinID FROM protein"
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    proteinlist = cursor.fetchall()
    protlist = list(proteinlist)

    protdrug = {}
    for protid in protlist:
        protidstr = "".join(protid)
        stmt2 = "SELECT D.drugID FROM protein P INNER JOIN proteinreaction PR on "
        stmt2 += "P.proteinID=PR.proteinID INNER JOIN reaction R on "
        stmt2 += "PR.reactionID=R.reactionID INNER JOIN partof PO on "
        stmt2 += "R.reactionID=PO.reactionID INNER JOIN drug D on "
        stmt2 += "PO.drugID=D.drugID WHERE P.proteinID like '"+protidstr+"'"

        cursor = connection.cursor()
        cursor.execute(stmt2)
        connection.commit()
        druglist = cursor.fetchall()
        ss = ""
        for l in druglist:
            ss += str(l)
        protdrug[protid] = str(ss)

    return protdrug


def get_proteins_binding_same_drug():  # 14
    stmt = "SELECT drugID FROM drug"
    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    druglist = cursor.fetchall()

    drugprot = {}
    for drugid in druglist:
        drugidstr = "".join(drugid)
        stmt2 = "SELECT D.drugID FROM drug D INNER JOIN partof PO "
        stmt2 += "on D.drugID=PO.drugID INNER JOIN reaction R on "
        stmt2 += "PO.reactionID=R.reactionID INNER JOIN proteinreaction PR "
        stmt2 += "on PR.reactionID=R.reactionID INNER JOIN protein P on "
        stmt2 += "P.proteinID=PR.proteinID WHERE D.drugID='"+drugidstr+"'"

        cursor = connection.cursor()
        cursor.execute(stmt2)
        connection.commit()
        druglist = cursor.fetchall()
        drugprot[drugid] = str(druglist)
        ss = ""
        for l in druglist:
            ss += str(l)
            drugprot[drugid] = str(ss)
    return drugprot

def get_drugs_with_side_effect(umls_cui): #15
    stmt = "SELECT D.drugID, D.drug_name "
    stmt += "FROM drug D INNER JOIN causes C on D.drugID=C.drugID INNER JOIN "
    stmt += "sideeffects S on C.umls_cui=S.umls_cui "
    stmt += "WHERE S.umls_cui = '" + umls_cui+"'"

    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    result = cursor.fetchall()
    return result

def get_search_description(keyword): #16
    stmt = "SELECT D.drugID, D.drug_name, D.description "
    stmt += "FROM drug D "
    stmt += "WHERE D.description LIKE '%" + keyword + "%'"

    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    result = cursor.fetchall()
    return result

def get_find_least_side(proteinid): #17
    stmt = ""
    stmt += "SELECT D.drugID, D.drug_name, S.side_name "
    stmt += "FROM protein P INNER JOIN proteinreaction R on P.proteinID = "
    stmt += "R.proteinID INNER JOIN partof O on R.reactionID = O.reactionID "
    stmt += "INNER JOIN drug D on O.drugID=D.drugID INNER JOIN causes C on D.drugID= "
    stmt += "C.drugID INNER JOIN sideeffects S on C.umls_cui=S.umls_cui "
    stmt += "WHERE P.proteinID ='"+proteinid+"' "
    stmt += "GROUP BY D.drugID"

    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    result = cursor.fetchall() # (('d1', 'dname1', 'side1'), ('d2', 'dname2', 'side1'))

    result = [[j for j in i] for i in result]

    l = []
    mincount = 0
    min = ""
    y = ""
    for i in result:
        if not y == i[0]:
            count = 0
            y = i[0]
        else:
            count +=1
            if mincount >= count:
                mincount = count
                min = y




    #l1 = {}
    #for i in result:
    return result


def get_doi_authors(): #18
    stmt = "SELECT F.doi, F.authors FROM foundby F"

    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    result = cursor.fetchall()
    return result

def get_ranking(): #19
    stmt = "SELECT S.institutionname, S.score "
    stmt += "FROM institution I "
    stmt += "ORDER BY S.score DESC;"

    cursor = connection.cursor()
    cursor.execute(stmt)
    connection.commit()
    result = cursor.fetchall()

    return result



def get_add_author(authors, reactioni):
    #stmt = "SELECT F.authors FROM foundby F WHERE F.reactionid=" + str(reactioni)
    #cursor = connection.cursor()
    #cursor.execute(stmt)
    #connection.commit()
   # result = cursor.fetchall()
  #  resultstr = str(result[0])[2:-3]
 #   print(resultstr)

#    resultstr += ";" + author

    stmt2 = "UPDATE foundby F SET F.authors='"+authors+"' WHERE F.reactionid=" + str(reactioni)
    cursor = connection.cursor()
    cursor.execute(stmt2)

