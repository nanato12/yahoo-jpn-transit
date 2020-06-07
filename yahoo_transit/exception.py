"""

Exception class

©︎ nanato12

"""

class NotFoundStationException(Exception):
    """
        search result not found station
    """

class NotFoundPrevTransit(Exception):
    """
        search result not found prev transit
    """

class NotFoundNextTransit(Exception):
    """
        search result not found next transit
    """
