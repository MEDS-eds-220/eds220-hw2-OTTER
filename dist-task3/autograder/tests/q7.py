OK_FORMAT = True

test = {   'name': 'q7',
    'points': 2,
    'suites': [   {   'cases': [{'code': ">>> assert pd.read_csv('data/t3_q7_df.csv', index_col='date', parse_dates=True).equals(aqi_sb)\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
