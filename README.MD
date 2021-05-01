# Experimental Design
The design was a 3x2 within-subject factorial design. The first IV (Authenticity) had 
3 levels (low, medium and high). The second IV (Verify) had 2 levels (verified and non-verified purchase).
The dependent variable (DV) was helpfulness rating on a scale from 1 to 5.
To improve the external validity of our results and, thus, be able to generalize our findings, we randomly sampled 10 products, 5 for the search product category and 
5 for the experience product category.
For each product, we randomly sampled 6 reviews, one for each level of the 2 
independent variables.
There were 6 conditions since there were 3 levels of Authenticity and 2 levels of 
Verify - i.e., 3(Authenticity)x2(Verify) = 6(conditions).
We run an online experiment on Mechanical Turk and recruited 162 participants.
The sample size was calculated for power= .80, alpha= 0.05 and a medium effect size (f= .25) using the package pwr2 for the r programming language*.
*https://cran.r-project.org/web/packages/pwr2/index.html
In the experiment, participants were allocated to all the 6 conditions for all the 10 products (i.e., 60 reviews in total). We counterbalanced the order of
the presentation of the conditions by using the lating square method.
For the analysis, we averaged the score given by the participants for multiple reviews in each condition (i.e., 10 reviews).

# Technology Stack
## Frontend
* jQuery

## Backend
* Flask
* Waitress

## Database Connector
* PyMySQL

## Database
* MySQL

## Deployment
* Aliyun ECS

## Experiment Platform
Amazon Mechanical Turk