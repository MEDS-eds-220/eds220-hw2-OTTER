OK_FORMAT = True

test = {   'name': 'q8',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> rolling_average_df = pd.DataFrame(rolling_average)\n'
                                               ">>> pd.read_csv('data/t3_q8_df.csv', index_col='date', parse_dates=True).equals(rolling_average_df)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> solution = pd.read_csv('data/t3_q9_df.csv', index_col='date')\n"
                                               '>>> solution.index = pd.to_datetime(solution.index)\n'
                                               '>>> assert aqi_sb.equals(solution)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
