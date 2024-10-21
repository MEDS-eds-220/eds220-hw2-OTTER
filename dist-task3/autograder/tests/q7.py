OK_FORMAT = True

test = {   'name': 'q7',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q7(aqi_sb):\n'
                                               '...     try:\n'
                                               "...         expected_data = pd.read_csv('data/t3_q7_df.csv')\n"
                                               '...         expected_data.date = pd.to_datetime(expected_data.date)\n'
                                               "...         expected_data = expected_data.set_index('date')\n"
                                               '...         pd.testing.assert_frame_equal(expected_data, aqi_sb)\n'
                                               '...     except AssertionError:\n'
                                               "...         raise AssertionError('Incorrect answer.')\n"
                                               '>>> test_q7(aqi_sb)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
