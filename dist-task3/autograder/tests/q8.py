OK_FORMAT = True

test = {   'name': 'q8',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> rolling_average_df = pd.DataFrame(rolling_average)\n>>> pd.read_csv('data/t3_q8_df.csv', index_col='date').equals(rolling_average_df)\nFalse",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> pd.read_csv('data/t3_q9_df.csv', index_col='date').equals(aqi_sb)\nFalse", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
