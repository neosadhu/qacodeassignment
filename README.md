# QA Code Assignment


This repository contains the testcases written in excel file along with an automated
python test script that will call the API with different types of 
tests and create a HTML report based on the result of the tests. 

#SCOPE: 
The scope of this testing activity was to perform some exploratory 
testing and record the results. 
A basing sanity testing and smoke testing of the API was performed
which included testing for the happy path as well as some
negative and invalid scenarios. 

Due to the limited time and resources of this testing exercise
Majority of the tests have an automated testing added to them
however there are still some manual tests that are not fully
automated. 

There were no load testing and performance testing involved. 
#AUTOMATED TESTS

IN ORDER TO RUN THE TESTS. 
1. Install Python 3.9 
2. Setup you environment PATH and PYTHONPATH variable to 
point to the Python executable.
3. Clone the branch. 
4. Install all the python dependencies using pip install -r requirements.txt
5. execute the tests using pytest tests/ --html-report=report.html
6. Collect the report.html and verify all the PASSES AND FAILURES


#REPORT
The report is an open source user friendly HTML report that can
be added to the python project. The report shows high level
pass/fail status as well as a some other metrics used to gauge
the status of the test cases. 
