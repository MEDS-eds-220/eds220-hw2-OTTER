OK_FORMAT = True

test = {   'name': 'q9',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> solution = pd.read_csv('data/t3_q9_df.csv', index_col='date')\n"
                                               '>>> solution.index = pd.to_datetime(solution.index)\n'
                                               '>>> assert aqi_sb.equals(solution)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
