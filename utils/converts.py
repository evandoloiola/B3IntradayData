import pytz
from datetime import datetime
from time import gmtime, mktime, strptime

def to_gmtime(ts):
    ''' Convert timestamp (13 digits support) to datetime local Time zone
    '''
    # set time zone
    local_tz = pytz.timezone ("America/Sao_Paulo")
    date = ts/1000
    return datetime.fromtimestamp(date,tz=local_tz)

def to_ts(dt):
    ''' From strftime to timestamp (13 digits support)'''
    return int(mktime(strptime(dt, "%Y-%m-%d %H:%M")) * 1000)
