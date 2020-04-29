import pandas as pd
from database.conn import connect_mysql, engine_mysql
from pandas.io import sql


class mysql_dao():
    """
    DAO - mysql databases conections
    All data bases operations
    """

    def __init__(self):
        pass

    def save_quotes_reg(self, date, price, low, high, var, varpct, vol):
        ''' save quotes one by one
        '''
        connection = connect_mysql()
        cursor = connection.cursor()
        query = """
        INSERT INTO 
            `quotes` 
            (`id`,
             `date`,
              `price`,
              `low`,
              `high`,
              `var`,
              `varpct`,
              `vol`)
              VALUES 
              (NULL,
               '{}',
               '{}',
               '{}',
               '{}',
               '{}',
               '{}',
               );
        """.format(
            price,
            low,
            high,
            var,
            varpct,
            vol
            )
        cursor.execute(query)
        cursor.commit()

    def save_quotes_list(self, data_list):
        ''' Save quotes in mysql from one list
        '''
        df = pd.DataFrame(data_list)
        connection = connect_mysql()
        cursor = connection.cursor()
        query = "INSERT INTO `quotes` (`id`,`date`,`price`,`low`,`high`,`var`,`varpct`,`vol`) VALUES (NULL,'%s','%s','%s','%s','%s','%s','%s','%s')" %(df['tricker'],df['date'],df['price'],df['low'],df['high'],df['var'],df['varpct'],df['vol'])
        print(query)
        cursor.execute(query)
        cursor.close()
        connection.commit()

    def save_quotes_pandas(self, df):
        ''' Save quotes in mysql from pandas data frame
        '''
        engine = engine_mysql()
        df.to_sql(con=engine, name='quotes', if_exists='append')
    
    def get_assets_list(self, *driver):
        ''' returns a pandas DataFrame with all data
        from trickers table in mysql
        driver: optinal (default:0)  'sqlalchemy' or 'pymysql'
        '''
        #sqlalchemy
        if driver == 'sqlalchemy':

            engine = engine_mysql()
            df = pd.read_sql('SELECT * FROM trickers', con=engine)
            return df
        #pymaysql
        elif driver == 'pymysql':
            
            connection = connect_mysql()
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM `trickers`')
            trickers = cursor.fetchall()
            df = pd.DataFrame(trickers)
            return df
        #default
        else:
            engine = engine_mysql()
            df = pd.read_sql('SELECT * FROM trickers', con=engine)
            return df