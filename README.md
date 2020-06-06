# yahoo-jpn-transit
Yahoo! unoffficial transit api

## Description
Yahoo!乗り換え案内の非公式APIです。

主に情報はスクレイピングにより取得しています。

検索時に駅名サジェストを行い、駅名を確立しているので曖昧検索にも対応しています。

## Example
```python
from datetime import datetime
from yahoo_transit import Transit

transit = Transit()
result = transit.search('桜木町', '横浜')

print(result)
# {'from': '桜木町', 'to': '横浜', 'datetime': datetime.datetime(2020, 6, 7, 4, 0, 29, 72139), 'simple_routes': [{'time': '3分', 'time_from': '04:18', 'time_to': '04:21', 'price': '136円', 'transfer': '乗換：0回', 'priority': ['[早]', '[楽]', '[安]'], 'reserve': None}, {'time': '3分', 'time_from': '04:32', 'time_to': '04:35', 'price': '136円', 'transfer': '乗換：0回', 'priority': ['[楽]', '[安]'], 'reserve': None}, {'time': '3分', 'time_from': '04:44', 'time_to': '04:47', 'price': '136円', 'transfer': '乗換：0回', 'priority': ['[楽]', '[安]'], 'reserve': None}]}

result = transit.search('さくらぎち', '横浜', datetime(2020, 6, 6, 23, 0))

print(result)
# {'from': '桜木町', 'to': '横浜', 'datetime': datetime.datetime(2020, 6, 6, 23, 0), 'simple_routes': [{'time': '4分', 'time_from': '23:00', 'time_to': '23:04', 'price': '136円', 'transfer': '乗換：0回', 'priority': ['[早]', '[楽]', '[安]'], 'reserve': None}, {'time': '3分', 'time_from': '23:05', 'time_to': '23:08', 'price': '210円', 'transfer': '乗換：0回', 'priority': ['[楽]'], 'reserve': None}, {'time': '3分', 'time_from': '23:08', 'time_to': '23:11', 'price': '136円', 'transfer': '乗換：0回', 'priority': ['[楽]', '[安]'], 'reserve': None}]}
```
