"""

Request class
Extend Scrap and Config class

©︎ nanato12

"""

# third party
import requests

# local
from .scrap import Scrap, url_parse
from .config import Config
from .exception import (
    NotFoundStationException
)

class Req(Scrap, Config):

    dt = None

    def __init__(self):
        Scrap.__init__(self)

    def get_suggest(self, keyword):
        res = requests.get(
            url=self.SUGGEST_URL,
            params={'q': url_parse.quote(keyword)}
        )
        return res.json()

    def get_result(self, from_, to, dt):
        self.set_datetime(dt)
        suggest = self.get_suggest(from_)
        if 'Station' not in suggest:
            raise NotFoundStationException('出発駅が見つかりませんでした。')
        flatron = ',,{code}'.format(code=suggest['Station'][0]['Code'])
        self.RESULT_PARAMS['flatron'] = flatron
        self.RESULT_PARAMS['from'] = suggest['Station'][0]['Suggest']
        self.RESULT_PARAMS['to'] = to
        res = requests.get(
            url=self.RESULT_URL,
            params=self.RESULT_PARAMS
        )
        result = {
            'from': self.RESULT_PARAMS['from'],
            'to': self.RESULT_PARAMS['to'],
            'datetime': self.dt,
            **self.scrap_result(res.text)
        }
        return result

    def set_datetime(self, dt):
        """
            set datetime in RESULT_PARAMS
        """
        self.dt = dt
        minites = self.dt.strftime('%M')
        self.RESULT_PARAMS['y'] = str(dt.year)
        self.RESULT_PARAMS['m'] = '{:0=2}'.format(dt.month)
        self.RESULT_PARAMS['d'] = '{:0=2}'.format(dt.day)
        self.RESULT_PARAMS['hh'] = '{:0=2}'.format(dt.hour)
        self.RESULT_PARAMS['m1'] = minites[0]
        self.RESULT_PARAMS['m2'] = minites[1]
