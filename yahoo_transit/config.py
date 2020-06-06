"""

Config class

©︎ nanato12

"""

class Config:

    """
        Value required when sending a request
    """

    HOST = 'https://transit.yahoo.co.jp'
    SUGGEST_URL = HOST + '/suggest/list.php'
    RESULT_URL = HOST + '/search/result'

    RESULT_PARAMS = {
        'fromgid': '',
        'togid': '',
        'viacode': '',
        'via': '',
        'viacode': '',
        'via': '',
        'viacode': '',
        'via': '',
        'type': '1',
        'ticket': 'ic',
        'expkind': '1',
        'ws': '3',
        's': '0',
        'al': '1',
        'shin': '1',
        'ex': '1',
        'hb': '1',
        'lb': '1',
        'sr': '1',
        'kw': ''
    }
