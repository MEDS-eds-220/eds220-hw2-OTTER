# EDS 220 - Assignment 2, tasks 2 and 3 - OTTER GRADER FILES

This respository contains materials to set up the [otter grader](https://otter-grader.readthedocs.io/en/latest/) for the second assignment for the course [EDS 220 - Working with Environmental Datasets](https://meds-eds-220.github.io/MEDS-eds-220-course/). This course is part of the [UCSB Masters in Environmental Data Science](https://bren.ucsb.edu/masters-programs/master-environmental-data-science).

### Repository Contents: 
      └── data/                                      # contains all data needed to run the notebook, csvs that start with                                                          t2 or t3 are used in the otter tests to check if the student's       
                                                       solution matches the csv with the solution
        └── daily_aqi_by_county_2017.csv           # aqi data for 2017, data used for task 3
        └── daily_aqi_by_county_2087.csv           # aqi data for 2018, data used for task 3
        └── salmon.csv                             # salmon data, data used for task 2
        └── t2_q2_df.csv                           # solution dataframe for task 2 question 2
        └── t2_q5_df.csv                           # solution dataframe for task 2 question 5
        └── t2_q6_df.csv                           # solution dataframe for task 2 question 6
        └── t2_q7_df.csv                           # solution dataframe for task 2 question 7
        └── t2_q8_df.csv                           # solution dataframe for task 2 question 8
        └── t3_q3a_df.csv                          # solution dataframe for task 3 question 3a
        └── t3_q3b_df.csv                          # solution dataframe for task 3 question 3b
        └── t3_q4_df.csv                           # solution dataframe for task 3 question 4
        └── t3_q6a_df.csv                          # solution dataframe for task 3 question 6a
        └── t3_q7_df.csv                           # solution dataframe for task 3 question 7, this test was not used in                                                         gradescope as it suddenly started to fail after running properly
        └── t3_q8_df.csv                           # solution dataframe for task 3 question 8
        └── t3_q9_df.csv                           # solution dataframe for task 3 question 9


            
    └── dist-task2/                                        
        └── autograder/                                              
            └── data/                                      # contains all data needed to run the notebook, csvs that start                                                               with t2 or t3 are used in the otter tests to check if the                                                                   student's solution matches the csv with the solution
                └── daily_aqi_by_county_2017.csv           # aqi data for 2017, data used for task 3
                └── daily_aqi_by_county_2087.csv           # aqi data for 2018, data used for task 3
                └── salmon.csv                             # salmon data, data used for task 2
                └── t2_q2_df.csv                           # solution dataframe for task 2 question 2
                └── t2_q5_df.csv                           # solution dataframe for task 2 question 5
                └── t2_q6_df.csv                           # solution dataframe for task 2 question 6
                └── t2_q7_df.csv                           # solution dataframe for task 2 question 7
                └── t2_q8_df.csv                           # solution dataframe for task 2 question 8
                └── t3_q3a_df.csv                          # solution dataframe for task 3 question 3a
                └── t3_q3b_df.csv                          # solution dataframe for task 3 question 3b
                └── t3_q4_df.csv                           # solution dataframe for task 3 question 4
                └── t3_q6a_df.csv                          # solution dataframe for task 3 question 6a
                └── t3_q7_df.csv                           # solution dataframe for task 3 question 7, this test was not    
                                                             used in gradescope as it suddenly started to fail after       
                                                             running properly
                └── t3_q8_df.csv                           # solution dataframe for task 3 question 8
                └── t3_q9_df.csv                           # solution dataframe for task 3 question 9

            └── tests/                                     # this folder contains all the individual tests as .py files, this folder is automatically created when                                                                     running otter assign
                └── q2a.py                                # .py test file for question 2a
                └── q2b.py                                # .py test file for question 2b
                └── q5.py                                 # .py test file for question 5
                └── q6.py                                 # .py test file for question 6
                └── q7.py                                 # .py test file for question 7
                └── q8.py                                 # .py test file for question 8
                
            └──hwk2-task2-salmon-autograder_2024_10_21T12_08_55_333407.zip   # this is the task 2 zip file for the     
                                                                               gradescope autograder configuration, this                                                                                   file gets uploaded directly into gradescope
            └── hwk2-task2-salmon.ipynb                   # this is the task 2 notebook with solutions (no tests), it is                                                                used to uploaded to gradescope as a test file to ensure all                                                                 tests are properly working
        └── student/
            └── data/                                     # contains all data needed to run the notebook, csvs that start                                                               with t2 or t3 are used in the otter tests to check if the                                                                   student's solution matches the csv with the solution
                └── daily_aqi_by_county_2017.csv          # aqi data for 2017, data used for task 3
                └── daily_aqi_by_county_2087.csv          # aqi data for 2018, data used for task 3
                └── salmon.csv                            # salmon data, data used for task 2
                └── t2_q2_df.csv                          # solution dataframe for task 2 question 2
                └── t2_q5_df.csv                          # solution dataframe for task 2 question 5
                └── t2_q6_df.csv                          # solution dataframe for task 2 question 6
                └── t2_q7_df.csv                          # solution dataframe for task 2 question 7
                └── t2_q8_df.csv                          # solution dataframe for task 2 question 8
                └── t3_q3a_df.csv                         # solution dataframe for task 3 question 3a
                └── t3_q3b_df.csv                         # solution dataframe for task 3 question 3b
                └── t3_q4_df.csv                          # solution dataframe for task 3 question 4
                └── t3_q6a_df.csv                         # solution dataframe for task 3 question 6a
                └── t3_q7_df.csv                          # solution dataframe for task 3 question 7, this test was not    
                                                             used in gradescope as it suddenly started to fail after       
                                                             running properly
                └── t3_q8_df.csv                          # solution dataframe for task 3 question 8
                └── t3_q9_df.csv                          # solution dataframe for task 3 question 9
           └── tests/                                     # this folder contains all the individual tests as .py files,                                                                 this folder is automatically created when running otter assign
                └── q2a.py                                # .py test file for question 2a
                └── q2b.py                                # .py test file for question 2b
                └── q5.py                                 # .py test file for question 5
                └── q6.py                                 # .py test file for question 6
                └── q7.py                                 # .py test file for question 7
                └── q8.py                                 # .py test file for question 8
           └── hwk1-task2-corals.ipynb                   # this is the notebook that should be distrubted to the students,                                                             all solutions are removed and all tests have been manually                                                                  deleted within the notebook, but are public to students on                                                                  gradescope     
    └── dist-task3/                                        
        └── autograder/                                              
            └── data/                                     # contains all data needed to run the notebook, csvs that start                                                               with t2 or t3 are used in the otter tests to check if the                                                                   student's solution matches the csv with the solution
                └── daily_aqi_by_county_2017.csv          # aqi data for 2017, data used for task 3
                └── daily_aqi_by_county_2087.csv          # aqi data for 2018, data used for task 3
                └── salmon.csv                            # salmon data, data used for task 2
                └── t2_q2_df.csv                          # solution dataframe for task 2 question 2
                └── t2_q5_df.csv                          # solution dataframe for task 2 question 5
                └── t2_q6_df.csv                          # solution dataframe for task 2 question 6
                └── t2_q7_df.csv                          # solution dataframe for task 2 question 7
                └── t2_q8_df.csv                          # solution dataframe for task 2 question 8
                └── t3_q3a_df.csv                         # solution dataframe for task 3 question 3a
                └── t3_q3b_df.csv                         # solution dataframe for task 3 question 3b
                └── t3_q4_df.csv                          # solution dataframe for task 3 question 4
                └── t3_q6a_df.csv                         # solution dataframe for task 3 question 6a
                └── t3_q7_df.csv                          # solution dataframe for task 3 question 7, this test was not    
                                                             used in gradescope as it suddenly started to fail after       
                                                             running properly
                └── t3_q8_df.csv                          # solution dataframe for task 3 question 8
                └── t3_q9_df.csv                          # solution dataframe for task 3 question 9
            └── tests/                                    # this folder contains all the individual tests as .py files,     
                                                            this folder is automatically created when running otter assign                                                              in the terminal
                └── q3_a.py                               # .py test file for question 3a
                └── q4.py                                 # .py test file for question 4
                └── q6_c.py                               # .py test file for question 6c
                └── q6_a.py                               # .py test file for question 6a
                └── q8.py                                 # .py test file for question 8
                └── q9.py                                 # .py test file for question 9
            └── hwk2-task3-aqi-autograder_2024_10_22T16_19_26_362655.zip  # this is the task 3 zip file for the gradescope                                                            autograder configuration, this file gets uploaded into gradescope                                                                                       
            └── hwk2-task3-aqi.ipynb                       # this is the task 3 notebook with solutions (no tests), it is                                                                used to uploaded to gradescope as a test file to ensure all                                                                 tests are properly working    
        └── student/
            └── data/                                     # contains all data needed to run the notebook, csvs that start                                                               with t2 or t3 are used in the otter tests to check if the                                                                   student's solution matches the csv with the solution
                └── daily_aqi_by_county_2017.csv          # aqi data for 2017, data used for task 3
                └── daily_aqi_by_county_2087.csv          # aqi data for 2018, data used for task 3
                └── salmon.csv                            # salmon data, data used for task 2
                └── t2_q2_df.csv                          # solution dataframe for task 2 question 2
                └── t2_q5_df.csv                          # solution dataframe for task 2 question 5
                └── t2_q6_df.csv                          # solution dataframe for task 2 question 6
                └── t2_q7_df.csv                          # solution dataframe for task 2 question 7
                └── t2_q8_df.csv                          # solution dataframe for task 2 question 8
                └── t3_q3a_df.csv                         # solution dataframe for task 3 question 3a
                └── t3_q3b_df.csv                         # solution dataframe for task 3 question 3b
                └── t3_q4_df.csv                          # solution dataframe for task 3 question 4
                └── t3_q6a_df.csv                         # solution dataframe for task 3 question 6a
                └── t3_q7_df.csv                          # solution dataframe for task 3 question 7, this test was not    
                                                             used in gradescope as it suddenly started to fail after       
                                                             running properly
                └── t3_q8_df.csv                          # solution dataframe for task 3 question 8
                └── t3_q9_df.csv                          # solution dataframe for task 3 question 9
           └── tests/                                     # this folder contains all the individual tests as .py files,     
                                                            this folder is automatically created when running otter assign                                                              in the terminal
                └── q3_a.py                               # .py test file for question 3a
                └── q4.py                                 # .py test file for question 4
                └── q6_c.py                               # .py test file for question 6c
                └── q6_a.py                               # .py test file for question 6a
                └── q8.py                                 # .py test file for question 8
                └── q9.py                                 # .py test file for question 9
           └── hwk2-task3-aqi.ipynb                      # this is the notebook that should be distrubted to the students,                                                             all solutions are removed and all tests have been manually                                                                  deleted within the notebook, but are public to students on                                                                  gradescope                                                                                                               
        
    └── .gitignore                  
    └── LICENSE
    └── hwk1-task2-salmon.ipynb                           # this is the master notebook for task 2, it contains all s                                                                   solutions and tests, this notebook is used to generate the                                                                  student notebook and all necessary files for the assignemnt
    └── hwk1-task3-aqi.ipynb                              # this is the master notebook for task 2, it contains all s                                                                   solutions and tests, this notebook is used to generate the                                                                  student notebook and all necessary files for the assignemnt
    └── README.md                                    
