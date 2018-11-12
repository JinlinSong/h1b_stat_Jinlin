# InsightDataScience/h1b_statistics

Original problem introductions: https://github.com/InsightDataScience/h1b_statistics

## Table of Contents
1. [Problem]
2. [Approach]
3. [Output]


## Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis).

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the `input` directory, running the `run.sh` script should produce the results in the `output` folder without needing to change the code.

## Approach

Raw data could be found [here](https://www.foreignlaborcert.doleta.gov/performancedata.cfm) under the __Disclosure Data__ tab (i.e., files listed in the __Disclosure File__ column with ".xlsx" extension).
### For given year data, we convert ".xlsx" into ".csv";
### Based on dataset header, we extracted related columns, including "case status", "working states", and "occupations", and remove records which are not certified;
### Based on "working states", we calculate the number of applications, getting the top 10 states with certified visa applications
### Based on "woccupations", we calculate the number of applications, getting the top 10 occupations with certified visa applications


## Output 
2 output files:
* `top_10_occupations.txt`: Top 10 occupations for certified visa applications
* `top_10_states.txt`: Top 10 states for certified visa applications

