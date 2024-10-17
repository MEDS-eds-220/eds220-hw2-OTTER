OK_FORMAT = True

test = {   'name': 'q5',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> len(catch_I) == 1\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(catch_I.iloc[0, 1] == 1955)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(catch_I.iloc[0, 0] == 'GSE')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(catch_I.iloc[0, 3] == 'I')\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
