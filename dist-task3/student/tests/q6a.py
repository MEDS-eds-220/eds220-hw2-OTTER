OK_FORMAT = True

test = {   'name': 'q6a',
    'points': 2,
    'suites': [   {   'cases': [{'code': ">>> pd.testing.assert_frame_equal(pd.read_csv('data/t3_q6a_df.csv'), aqi_sb.reset_index(drop=True))\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
