import pymysql

# Database Connection
def connect_db():
    return pymysql.connect(host='localhost',
                       user='root',
                       password='12qwaszX!',
                       db='amazon_review')

import uuid

def store_userInfo(userData_dict):
    conn = connect_db()
    with conn.cursor() as cursor:
        sql = "INSERT INTO user (age, gender, use_amazon, read_review, created) VALUES ('{}','{}','{}','{}', NOW()); ".format(
                userData_dict['age'],
                userData_dict['gender'],
                userData_dict['use_amazon'],
                userData_dict['read_review']
            )

        print("sql", sql)
        cursor.execute(sql)
        conn.commit()

        cursor.close()

    with conn.cursor() as cursor:
        sql = "SELECT LAST_INSERT_ID();"
        cursor.execute(sql)
        result = cursor.fetchall()

        cursor.close()
        return result[0][0]

    conn.close()

def store_agreement(agreementData_dict):
    conn = connect_db()
    with conn.cursor() as cursor:
        sql = "Update user SET agreement = 'Y' WHERE id = '{}'".format(
                agreementData_dict['id']
            )

        print("sql", sql)
        cursor.execute(sql)
        conn.commit()

        cursor.close()
    conn.close()