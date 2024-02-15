[Lending Club A](https://services.hbsp.harvard.edu/api/courses/1122752/items/119021-PDF-ENG/sclinks/4c836fd15436ffb1913c9d6905c276ca)


[Lending Club B](https://services.hbsp.harvard.edu/api/courses/1122752/items/119022-PDF-ENG/sclinks/8328cf7e8fa110d69a08247dc0c02448)
## Key Questions

1. What do you think of the random forest approach? Which model do you think Figel should choose? Why?

2. How does the gradient boosted tree (GBT) modeling approach differ from random forest and decision trees?

3. What do you make of the comparative feature impacts as shown in Table 3? What do these reveal about the mechanics of each model?

4. What decision should Figel make based on the confusion matrix and her analysis of payoffs? What else should Figel consider before making her decision?

5. Is Figel's analysis helpful for making better loan decisions, or should she simply use the loan classifications provided by LendingClub?

## Data Exercise:

Once you have prepared the data (train_loans2013_2015q1_minimalprocessing.csv and test_loans2013_2015q1_minimalprocessing.csv)  provided within the unit 4 live session preparation:

1. Create Decision Tree, Random Forest, Gradient Boosted Trees on your feature list and default feature list. How does logloss differ?

2. Explain 'Validation,' 'Cross Validation' and 'Holdout' - i.e. how many approximate samples are being used in each of those columns.

3. Take a look at Feature Impact, which are the top 3 features.
   1. dti, pct_tl_nvr_diq, & hardship_end_date are the top features of my goosted tree.

4. Utilize the test dataset to get predictions from DataRobot. You will utilize these predictions to submit to a Kaggle competition. The link to the Kaggle competition will be provided in the course Slack channel. You should submit actual probabilities as predictions (not class 1 or 0) to Kaggle.

For further assistance with the Kaggle submission/DataRobot, you may attend office hours.