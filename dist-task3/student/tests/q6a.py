OK_FORMAT = True

test = {   'name': 'q6a',
    'points': 2,
    'suites': [   {   'cases': [{'code': ">>> pd.read_csv('data/t3_q6a_df.csv').equals(aqi_sb.reset_index(drop=True))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
