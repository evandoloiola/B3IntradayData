from json import loads
from requests import get

def get_assets(self):
    ''' get assets from uol finance API
    '''
    # mk url's
    base = 'http://cotacoes.economia.uol.com.br/ws/asset'
    assets = base + '/stock/list?size=10000'
    assets = {i['code']: i['idt'] for i in get(assets).json()['data']}
    return assets

def get_intraday(asset):
    ''' Get data quotes from uol finiance API
    '''
    base = 'http://cotacoes.economia.uol.com.br/ws/asset'
    intraday = base + '/{asset}/intraday?size=600&callback=uolfinancecallback0'
    url = intraday.format(**{'asset': asset})
    return loads(get(url).content[20:-2])
