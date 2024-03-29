
## [Lending Club A](https://services.hbsp.harvard.edu/api/courses/1122752/items/119020-PDF-ENG/sclinks/b120e5540b508dfabfd526326094f712)

## [Lending Club B](https://services.hbsp.harvard.edu/api/courses/1122752/items/119021-PDF-ENG/sclinks/4c836fd15436ffb1913c9d6905c276ca)

1. Should Figel invest in LendingClub? Why or why not? 
   1. Figel has access to the company data and the ability to create models which will predict who should be given loans. Because there are $22,000,000 in loans that are did not meet the specified grade levels, there is room for her to identify a model which will appropriately accept loans and assign designated grade levels.

2. How should Figel prepare the data for her business problem? Which loans should she classify as defaulters from Table 1 in “LendingClub (A)”? Which feature variables should she use from Exhibit 6 of “LendingClub (A)”? Should she collect data on other variables? Should she create new variables such as debt-to-income ratio?
   1. Figel should use num_tl_120dpd_2m, delinq_2yrs, delinq_amnt, num_accts_ever_120_pd, acc_now_delinq, dti to classify defaulters. This will show the ratio of total monthly debt payments to total debt obligations, the number of 30+ days past-due incidences of delinquency in the borrower's credit file for the past 2 years, the amount owed for the accounts on which the borrower is now delinquent, the number of accounts currently 120 days past due, and the number of accounts every 120 or more days past due. Debt-to-income ratio is already listed as a variable in the dataset. 

3. What did you think of the decision tree model and pruning as an approach to identifying loans that will default/not default? What did you like about it? What were its weaknesses?
   1. The decision tree model and pruning approach allows for a methodical means to calculate decisions that are grounded in an objective mathematical metric called Gini impurity. It presents a reasonable approach to making data-driven decisions. Pruning the tree allows the ability to reduce the loss such that the tree is not overfit to the training data. This allows for results that are generalized sufficiently to accurately make predictions on test data. I personally enjoy the concept of an ensemble of models collectively working together to create a prediction. 

4. Look at the plots in “LendingClub (B)” Appendix Figure A-1. Could you imagine a different way to separate the defaulters and the repayers (nondefaulters) than the one presented using decision trees? 
   1. It is possible to linearly separate the original scatter plot in Figure A-1 with a vertical rather than horizontal line to separate repayers from defaulters. In doing so, I would select the income level of $80,000 to maximize the number of repayers right of the line from the number of defaulters left of the line. 