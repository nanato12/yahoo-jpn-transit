"""

Transit class
This is main class

©︎ nanato12

"""

# standard
from datetime import datetime

# local
from .req import Req

class Transit:

    def __init__(self):
        self.req = Req()

    def get_suggest(self, keyword):
        """
            get sugggest stations
        """
        return self.req.get_suggest(keyword)

    def search(self, from_, to, dt=None):
        """
            search transit
        """
        if dt is None:
            dt = datetime.now()
        return self.req.get_result(from_, to, dt)

    def get_prev_data(self):
        """
            get prev transit
        """
        return self.req.get_prev()

    def get_next_data(self):
        """
            get next transit
        """
        return self.req.get_next()
