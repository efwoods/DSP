# Live Session Preparation
[Predicting Purchasing Behavior at PriceMart (A)](https://services.hbsp.harvard.edu/api/courses/1122752/items/119025-PDF-ENG/sclinks/55674860382f064cc30608dc7e59ed27)

[Predicting Purchasing Behavior at PriceMart (B)](https://services.hbsp.harvard.edu/api/courses/1122752/items/119026-PDF-ENG/sclinks/570b8bbd69cb687c30a169bca7778310)

## Key Questions (A):
1. What business challenge were Wehunt and Morse trying to address? Do you think it is worth doing? 
   1. Wehunt & Morse were trying to predict if a customer was pregnant or trying to get pregnant based upon their purchases. By identifing if a customer household was preganant or trying to get pregnant, they could send targeted deals to the a select group of customers based upon their shopping habits knowing their intent to purchases items is in alignment with these predictions. This would help drive traffic away from their competitors. 

2. Wehunt and Morse collect data on several features and the target variable. How comfortable are you with the data they have collected? How might they have acquired the data with which to train their models? 
   1. I am comfortable with the data that they have collected if the data was collected with the awareness and consent of the customers in the household and the intent of its use was clearly indicated. The data could have been collected by keeping a database of online purchases that identify a customer's online profile with their spending history. 

3. What do you think about how Morse has gone about building the prediction and validation models? Do you think he should choose a balanced sample of pregnant/not pregnant households or simply keep the proportion of pregnant/not pregnant households in the population in the training sample? Should the validation sample be balanced or unbalanced?
      1. Answer: I think that he should choose a balanced sample of pregnant versus not pregnant households for the training set. The validation set may be left unbalanced. By having a balanced training set, the model will be trained to predict the outcome of the results of pregnant versus non-pregnant households where there are an equal number of examples that are exposed to the model. If the model was exposed to a single example of a pregnant household and a multitude of non-pregnant households in the extreme case, then the model would be a poor predictor when tested against the validation set. The validation set may be left unbalanced to represent the model's performance against a real population where the distribution of pregnant vs non-pregnant households are not necessarily equal.  

4. Should Morse use the linear regression model or the logistic regression model for making predictions? Why? 
   1. Morse should use the logistic regression model for making predictions because there is a lower log loss shown in Exhibit 6. The log loss is 0.1317 vs 0.1514 for an ordinary least squares regression which indicates that the logistic regression is a better fit to the data as indicated by less error. 

5. What further analysis should Wehunt and Morse do on Exhibit 6? Should they evaluate the signs of the coefficients, their magnitudes, and statistical significance? What should they do about coefficients that are not statistically significant? 
   1. Examining the model coefficients indicates the status of pregnancy with respect to the sign of the coefficient given that the coefficients are statistically significant. The magnitude indicates to what degree the coefficients indicate pregnancy status. It should be observed which coefficients are not statistically significant and afterwards, these coefficients may be safely ignored as predictive indicators of household pregnancy status. 

## Key Questions (B):

1. Does it make sense for Morse to regularize the coefficients of the logistic regression model? Wouldn’t this make the model worse? 
   1. Regularization of the coefficients of the logistic regression model prevents the coefficients from becoming too large and overfitting onto the training data which would result in error. 

2. Should Morse run different types of regularizations such as ridge and LASSO? Should Morse try to combine ridge and LASSO regression equations? Why? 
   1. Morse should run different types of regularizations such as ridge and Lasso to compare the accuracies of each model. He should not try to combine ridge and Lasso regression equations because they use separate methods for performing dimensionality reduction of the predictors. In a ridge regression, the coefficients are reduced near zero but never diminish predictors completely. Lasso regression will reduce the coefficients of predictors to zero which will result in a loss of the effect of those predictors on the predicted response. 

3. What is the benefit to Morse of developing the receiver-operator-characteristic (ROC) curve? Do you agree with the values Wehunt and Morse have developed for the payoff matrix (Table 4)? 
   1. The benefit to Morse of developing the receiver-operator-characteristic (ROC) curve is that is allows Morse to choose between a True Positive Rate and a False Positive Rate. In situations where false positives are not critical errors, the trade off between the TPR and FPR will allow for higher true positive accuracy at the expense of the presence of false positives. In contrast, the TPR may also be diminished to prevent the presence of false positives. I believe they should use a cutoff value of .4. Sending an advertisement to customers will at least promote Pricemart to the customers while increasing profit due to the increase in true positives. The false positive results may in an extreme case tarnish the reputation of PriceMart and lose customers who no longer trust PriceMart with their data or feel that their privacy has been violated. Given the context of the advertisement, I believe it is safe to assert that such an extreme case would not realistic. 

4. Is this analysis helpful to Wehunt to make decisions? How and why?
   1. This analysis allows Wehunt to determine how many ads to produce and distribute through a deterministic cost-benefit analysis. This forethought allows for the precise result of the ads to come to fruition as the advertisements are distributed to the correct proportion of individuals to maximize profit, retain customers, and minimize reputation loss.  