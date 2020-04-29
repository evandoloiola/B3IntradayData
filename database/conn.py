import pymysql
from sqlalchemy import create_engine
from json import loads
from requests import get

def connect_mysql():
    ''' connect to mysql data base
    Returns:
        Connetction string
    '''
    #load data base credencials from ./db.json
    json_file ='/db.json' 
    #load credencials
    host = get(json_file).json()['host']
    user = get(json_file).json()['user']
    password = get(json_file).json()['password']
    db = get(json_file).json()['db']

    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=db)
    return conn

def engine_mysql():
    engine = create_engine('mysql+pymysql://webizyco_fruya:#Atualidade#13@185.201.10.16/webizyco_fruya')
    return engine