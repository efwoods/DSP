

Key Questions for Case Reading and Peer Learning Session Discussion. Please review and answer on the following cards.

[(A):](https://services.hbsp.harvard.edu/api/courses/1122752/items/119023-PDF-ENG/sclinks/a48e580c9b5f5f1a72967f890e59d489)

1. What problem is Booth trying to address at Chateau? Is the data Booth is using helpful to address his problem? 
Booth is trying to sell underperforming wines at a discount to customers based on their purchase preferences. The quantity of alcohol purchased by customer during the interval of one year is pertinent information to address this problem. 

2. Is cluster analysis useful to Booth? Why?
   1. Cluster analysis is useful to Booth because it allows Booth to recognize which customers have a preference for which wine and offer them discounts. This will decrease the surplus of underperforming wine and increase the quality of life of customers who enjoy those particular brands of wine. 

3. Should Booth use Euclidean distance or cosine similarity in cluster analysis? Why?
   1. Booth should use Euclidean distance because he is dealing with the quantity of sales. 

4. Is the more complex deal-by-deal cluster analysis helpful to Booth for marketing wines in 2018? How could he use it? 
   1. Yes, the deal-by-deal cluster analysis provides a more detailed insight into the preferences of a customer. Where a customer may be interested in a particular brand of alcohol, that does not necessarily indicate that they have an interest in a deal on that brand due to a possible spurious reason such as income, habit, diet, etc. He can leverage the deal-by-deal cluster analysis to identify customers that are similar with respect to deals and notice other deals that customers who take deals that customers may be interested in based upon silhouette values. 

[(B):](https://services.hbsp.harvard.edu/api/courses/1122752/items/119024-PDF-ENG/sclinks/0cffa1fc9a19e19420b06d29840c7dcf)

1. How does the supervised approach differ from the unsupervised approach? 
   1. In the supervised learning approach, the predictions of an unknown purchase of a particular brand of alcohol were made based upon a chosen predictor. The unsupervised learning approach made predictions based upon likeness with respect to a given cluster.

2. Why might Booth want to do collaborative filtering? Is it better than clustering?
   1. Collaborative filtering allows for a prediction to be made with respect to a particular predictor which allows for domain knowledge to be applied to the problem. For example, when predicting the number of bottles of Malbec a new customer would purchase, this prediction may be made with respect to the historical purchases of other brands of alcohol, the similarity between the new customer's purchases and the purchases of other customers, and the ratio of another customer's purchase of a given brand of wine with respect to the wine to be purchased. This allows for the prediction to be explainable.

3. What choices must Booth make when using collaborative filtering? How should he decide?
   1. Booth must choose which customer to use for comparison and the brand of alcohol from which to make a prediction. He should decide based upon the highest value of cosine similarity of historical purchases of alcohol and his domain expertise in wine sales.

4. What is the difference between collaborative filtering with cosine similarity of customers from collaborative filtering with cosine similarity of products?
   1. In the cosine similarity of customers, it is possible to view how similar customers are to each other with respect to their tastes of alcohol. In the cosine similarity of products, it is shown which products customers found similar to each other.

5. How might Booth use the analysis of deal data for decision-making?
   1. The analysis of deal data may be used as labels for which to make a prediction on whether an individual will make a purchase given a new deal given a set of predictors which comprise that deal. For example, a logistic regression may be made using the deal data as the response and the alcohol that comprises each deal as the training data. Then, given a new set of brands of alcohol that are underperforming, the trained model may be applied to determine which individual would be most likely to accept the new deal.