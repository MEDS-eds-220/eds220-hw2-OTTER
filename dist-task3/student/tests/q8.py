OK_FORMAT = True

test = {   'name': 'q8',
    'points': 2,
    'suites': [   {   'cases': [{'code': ">>> pd.read_csv('data/t3_q8_df.csv', index_col='date', parse_dates=True).equals(pd.DataFrame(rolling_average))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
