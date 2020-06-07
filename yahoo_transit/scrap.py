"""

Scraping class

©︎ nanato12

"""

# standard
import urllib.parse as url_parse

# third party
from bs4 import BeautifulSoup

class Scrap:

    soup = None
    prev_info = None
    next_info = None

    def set_soup(self, html_text):
        self.soup = BeautifulSoup(html_text, 'html.parser')

    def scrap_result(self, response_text):
        self.set_soup(response_text)
        result = {}
        # simple_routes
        simple_routes = self.get_simple_routes()
        result['simple_routes'] = simple_routes
        # set prev_info, next_info
        self.set_prev_info()
        self.set_next_info()
        return result

    def get_simple_routes(self):
        routes = self.soup.find('ul', id='rsltlst')
        simple_routes = []
        for ul in routes.find_all('ul'):
            # print(ul)
            detail = {}
            # time element
            li_time = ul.find('li', class_='time')
            time = li_time.find('span', class_='small').text
            li_time_text = li_time.text.replace(time, '')
            # fare element
            li_fare = ul.find('li', class_='fare')
            price = li_fare.text
            # transfer element
            li_transfer = ul.find('li', class_='transfer')
            transfer = li_transfer.text
            # priority
            li_priority = ul.find('li', class_='priority')
            span_list = li_priority.find_all('span')
            priority = [span.text for span in span_list]
            # reserve
            li_reserve = ul.find('li', class_='reserve')
            if li_reserve is None:
                reserve = None
            else:
                reserve = li_reserve.text.replace('\n', '')
            # detail
            detail['time'] = time
            detail['time_from'] = li_time_text.split('→')[0]
            detail['time_to'] = li_time_text.split('→')[1]
            detail['price'] = price
            detail['transfer'] = transfer
            detail['priority'] = priority
            detail['reserve'] = reserve
            simple_routes.append(detail)
        return simple_routes

    def set_prev_info(self):
        li_prev = self.soup.find('li', class_='prev')
        prev_url = li_prev.find('a').get('href')
        if prev_url is None:
            return
        parse_result = url_parse.urlparse(prev_url)
        query_params = dict(url_parse.parse_qsl(parse_result.query))
        self.prev_info = {
            'path': parse_result.path,
            'params': query_params
        }

    def set_next_info(self):
        li_next = self.soup.find('li', class_='next')
        next_url = li_next.find('a').get('href')
        if next_url is None:
            return
        parse_result = url_parse.urlparse(next_url)
        query_params = dict(url_parse.parse_qsl(parse_result.query))
        self.next_info = {
            'path': parse_result.path,
            'params': query_params
        }
