OK_FORMAT = True

test = {   'name': 'q8',
    'points': 2,
    'suites': [   {   'cases': [{'code': ">>> pd.read_csv('data/t2_q8_df.csv', index_col='Region').round(4).equals(pd.DataFrame(avg_region.round(4)))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
