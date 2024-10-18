OK_FORMAT = True

test = {   'name': 'q4',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> aqi.equals(pd.concat([pd.read_csv('data/daily_aqi_by_county_2017.csv'), pd.read_csv('data/daily_aqi_by_county_2018.csv')]))\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
