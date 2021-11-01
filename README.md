# Project 3 Subreddit sentiments on Trader Joe's vs. Wholefoods

### Problem Statement

Trader Joe's and Wholefoods are two popular grocery chains who boast organic and sustainable products. They are different in many aspects in terms of product mix, private labels, store size and sourcing etc., but they are often considered as competitors. 
Why is this the case? The reason is because they shared the same customer. Over 95% of the customers will visit both stores for organic, healthy products. 

Pandemic has caused a loss in in-store visits for both stores, however, Trader Joe's has seen a recovery whereas Whole Food still lag behind. In the healthy-organic market showdown, Trader Joe's win the cake.

![alt text](https://shriyagettingsocial.files.wordpress.com/2014/02/whole-foods-vs-trader-joes.png "Logo Title Text 1")


The project is aimed to look the most recent subreddits on both stores and analyze the sentiments online. We will also utilize NLP and classification models to predict which a given post came from.
This would be the very first step for a customer churn for marketing analysis in future.

### For project 3, the following approach is followed:
1. **Data Collection:** Collect 1000 subreddits since 09/30/2021 on both store names: traderjoes vs wholefoods through subreddit API.
2. **EDA:** NPL analysis to count the word length of the title, and analyze the postivtiness of the posts in the whole data and compare the overall scores of the two stores.
3. **Modeling:** The data were train-test splited into train and test data sets. In the pipeline, the CountVectorizer() is responsible for NLP fit and transform, and 4 different classification models were explored. The best two models are : 1) MultinomialNB and 2) RandomForest Classifier.
4. **Voting:** Used the VotingClassifier to vote on the two best models and further improved the accuracy to 90%.


### Summary of model
In this project, two high-performed models have been explored, each one has its own pros and cons:
||Accuracy|Precision|Recall(pos=traderjoes)|
|---|---|---|---|
|**VotingClassifier**|0.9|0.93|0.86|
|**MultinomialNB**|0.88|0.87|0.9|
|**RandomForestClassifier**|0.88|0.93|0.83|

### Conclusion
**NPL Analysis:**
* Sentimental analysis showed the post length are about the same for both stores, but Trader Joe's won by a large margin on having more positive postS, and Trader Joe's also tends to have less negative posts as compared to Whole Foods.

In this project, two high-performed models have been explored, each one has its own pros and cons:
**Model recommendation should be tailored to customer need:**
* If the customer cares the total correctly prediction for both stores, VotingClassifier is recommended.
* If my customer cares more accurate prediction on Trader Joe's posts, in other word, a higher recall score for Trader Joes, Multinomial NB model is recommended.


