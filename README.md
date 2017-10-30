my-find-political-donors

Introduction

The project aims to  help identify possible donors for a variety of upcoming election campaigns according to https://github.com/InsightDataScience/find-political-donors.

The program was taken an input file that lists campaign contributions by individual donors and distilled it into two output files:

medianvals_by_zip.txt: contains a calculated running median, total dollar amount and total number of contributions by recipient and zip code

medianvals_by_date.txt: has the calculated median, total dollar amount and total number of contributions by recipient and date.

Approach and Dependencies 

The program is written by python. You need have a python environments. For an example, we need Python 3.6.3 or later version.
The program was involved in two packages : numpy and pandas.
Before we run the program, we need to install numpy http://www.numpy.org/ and pandas http://pandas.pydata.org/
We intall these two packages in a python environment and set the path.

Run Instructions
The input file should be named "itcont.txt" and put into "imput" folder
The script "run.sh" can be run in a command line to run the "Donor_analysis.py" in the src folder.
You can run the test with the following command:
~$ ./run.sh 

The test results are in insight_testsuite folder.
You can run the test with the following command from within the insight_testsuite folder:
insight_testsuite~$ ./run_tests.sh 
