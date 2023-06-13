#show tables: SQL Show Tables: List All Tables in a Database - Database Star
import pymysql #1. pip3 install --upgrade pip 2. pip3 install pymysql

import pandas as pd
import numpy as np
import collections
import itertools
from datetime import date, datetime, timedelta
import random


################ MySQL ###################
database = 'empresa'
username = 'root'
password = '1234'
db = pymysql.connect(host="127.0.0.1", user=username, passwd=password, database=database)
cursor = db.cursor()# prepare a cursor object using cursor() method

l=['\U00002639','\U0001F602','\U0001F602', '\U0001F609', '\U0001F60A']
def consulta():
    consulta = " SELECT nombre, salario, puesto from empleado " 
    print("consulta:", consulta)
    cursor.execute(consulta)
    df = pd.read_sql_query(consulta, db)
    df["salario$"]= df.salario.map(lambda x: str(x) + "$")
    print("type(df)=", type(df))
    print("df.info()=",df.info())
    print("df.describe()=",df.describe())
    print("df.head(10)=",df.head(10))
    print("df.tail(10)=",df.tail(10))
    print("df.sample(20)=",df.sample(20))
    df_nuevo= df.nombre.map(lambda x: str.upper(x))
    print("df_nuevo.head(10)=",df_nuevo.head(10))
    df2_nuevo=df.salario.map(lambda x: x*1.07)
    print("df_nuevo.head(10)=",df2_nuevo.head(10))
    df ["salario$"] = df.salario.map(lambda x: x*1.07)
    print("df.head(10)=",df.head(10))
    df = df.nombre.map(lambda x: random.choice(l)+x)
    print("df.head(21)=",df.head(21))
    df.to_excel("df.xlsx")
consulta()

'''def consulta_dept(): 
    consulta = " SELECT * from departamento "
    print("consulta:", consulta)
    cursor.execute(consulta)
    df = pd.read_sql_query(consulta, db)
    print("type(df)=", type(df))
    print("df.info()=",df.info())
    print("df.describe()=",df.describe())
    print("df.head(6)=",df.head(6))
    print("df.tail(6)=",df.tail(6))
   # print("df.sample(6)=",df.sample(6))
    df_dept = df.nombre.map(lambda x: str.upper(x))
    print("df_dept.head(10)= ", df_dept.head(10))
    import functools 
suma_sueldos=functools.reduce(lambda a, b: a+b, [tupla[6] for tupla in results]) #el segundo argumento es un  List comprehension
print("suma_sueldos=", suma_sueldos)
consulta_dept()'''
