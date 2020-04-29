import pandas as pd
import time
import logging
from datetime import datetime
from database.dao import mysql_dao
from uol.uol_api import get_intraday
#config logging
logging.basicConfig(filename='fruya.log',level=logging.DEBUG)
logging.info('----------' + datetime.now().strftime('%d/%m/%Y %H:%M:%S') + '----------------')
logging.info('Start application')
# verifica o tempo da carga de dados
ini = time.time()

dao = mysql_dao()

assets = dao.get_assets_list()
logging.debug('Assests are listed to begin get data')

if __name__ == '__main__':
    
    for index, asset in assets.iterrows():
        quote = get_intraday(asset['id']).get('data', {})
        df = pd.DataFrame(quote)
        df['tricker'] = asset['tricker']
        logging.debug('All ready to save ' + asset['tricker'] + ' on data base.')
        dao.save_quotes_pandas(df)
        logging.debug(asset['tricker'] + ' save -> data base.')
fim = time.time()
print (fim-ini)