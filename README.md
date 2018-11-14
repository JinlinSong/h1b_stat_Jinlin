# InsightDataScience/h1b_statistics

[Original problem introductions](https://github.com/InsightDataScience/h1b_statistics)

## Table of Contents
1. [Problem]
2. [Approach]
3. [Output]


## Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis).

You are asked to create a mechanism to analyze past years data, specifically calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the `input` directory, running the `run.sh` script should produce the results in the `output` folder without needing to change the code.

## Approach

Raw data could be found [here](https://www.foreignlaborcert.doleta.gov/performancedata.cfm) under the __Disclosure Data__ tab (i.e., files listed in the __Disclosure File__ column with ".xlsx" extension).
1. For the given year data, we convert ".xlsx" into ".csv";
2. Based on the dataset header, we extracted related columns, including "case status", "working states", and "occupations", and remove records which are not certified;
3. Based on "working states", we calculate the number of applications, getting the top 10 states with certified visa applications
4. Based on "occupations", we calculate the number of applications, getting the top 10 occupations with certified visa applications

## Running code

Place the input file as ./input/h1b_input.csv and run the run.sh script.


## Output 
2 output files:
* `top_10_occupations.txt`: Top 10 occupations for certified visa applications
* `top_10_states.txt`: Top 10 states for certified visa applications

## Challenges

1. The CSV header (column names) are different for different years, we should adjust parameters in h1b_stat.py under src folder state_column_name, occupation_column_name, status_column_name. If the certified application "status" is different with value 'CERTIFIED' for the new file, we should adjust certified_value as well; Before we run the run.sh, check file header, and check the certified application "status" value. For example year 2014, the parameters should be:
status_column_name = STATUS
state_column_name = LCA_CASE_WORKLOC1_STATE
occupation_column_name = LCA_CASE_SOC_NAME
certified_value = 'CERTIFIED'

2. There are missing data or typo in the original file. We are supposed to clean the data before analysis, avoiding obvious error.



