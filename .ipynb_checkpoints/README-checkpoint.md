# Summary - rating-prediction-google-local
Predict ratings of google local reviews in order to better recommend the places to users based on historical data and the sentiment within the reviews. We just used CA data (got the coordinates from [here](https://latitudelongitude.org/us/#:~:targetText=Lat%2Dlong%20coorditates%20for%20cities,from%20%2D161.75583%20to%20%2D68.01197.&targetText=Washington%2C%20D.C.,(Washington%2C%20D.C.))). You can try to use different coordinates and just reproduce the analysis and prediction and save it conveniently.

**How can rating prediction help for better recommentations?**

When people utilize online evaluations to make decisions, they need to look at various factors such as star ratings, review texts, locations, etc. Often times it is difficult for users to read through all reviews, decide which factors are important to them, and incorporate the related information to make final decisions. User experience would be highly improved if there is a recommender system that predicts ratings given a user and a place. If the ratings are predicted from the historical data, those models can be used to:

1. Build user profiles and make recommendations

2. Make item-based recommendations by setting thresholds on how user might rate similar items

3. Making recommendations by displaying top-N based on a condition on predicted rating ([An example](https://towardsdatascience.com/evaluating-a-real-life-recommender-system-error-based-and-ranking-based-84708e3285b))

**Data Source**: https://cseweb.ucsd.edu/~jmcauley/datasets.html#google_local

**In collaboration with**: [Shiyi Hua](https://www.linkedin.com/in/shiyi-letty-hua-2a7117129/), [Ziyuan Yan](https://www.linkedin.com/in/ziyuan-esther-yan-664732132/)

**Data dictionary**: The source link provides a good sense of what are all the fields we have.

**Visualization**: Though this is not a project which heavily depends on exploratory analysis and visualizations, we  have some basic visualizations and the code in [visualization.Rmd](https://github.com/akshayreddykotha/rating-prediction-google-local/blob/master/visualization.Rmd). You can also have a quick glance of what they are in the detailed [report](https://github.com/akshayreddykotha/rating-prediction-google-local/blob/master/project-report.pdf).

**Models**:

1. Trivial baseline (Avg. rating prediction): [model-00](https://github.com/akshayreddykotha/rating-prediction-google-local/blob/master/models/model-00.ipynb)

2. Bag-of-words in Ridge regression: [model-01](https://github.com/akshayreddykotha/rating-prediction-google-local/blob/master/models/model-01.ipynb)

3. Bag-of-words in Ridge regression + hour + price level + review length: [model-02](https://github.com/akshayreddykotha/rating-prediction-google-local/blob/master/models/model-02.ipynb). There are various variations of models in which features are encoded (like one-hot, categorical encoding of price level and hour).

4. Sentiment based rating prediction (positive + negative sentiments + hour + price level + review length): [model-03](https://github.com/akshayreddykotha/rating-prediction-google-local/blob/master/models/model-03.ipynb). Again this file has different variants ranging from using only proportion of sentences with positive and negative sentiments to having all the other features as well.

5. Sentiment based rating prediction (Bag of words (Top 1000) + positive + negative sentiments + hour + price level + review length): [model-04](https://github.com/akshayreddykotha/rating-prediction-google-local/blob/master/models/model-04.ipynb). This model has all the best consierations amongst the above models like encoded features for `priceRank`, `reviewHour`, and more granularity with respect to those reviews where a review didn't have more than one proper sentence.

**Other files**:

1. `exploration.ipynb` - This file is just to play with the data and understand the data structures if you are just starting. Might as well contain some errors if you have cloned and ran directly.

2. `functions.py` - Collection of functions I used in my models. Thought it would be helpful to have a separate file instead of getting lost while going through part of code.

3. `df_ca.csv` and `df_ca_02.csv` are intermediary files to create some exploratory visualizations in the .Rmd file.

For a detailed report of the entire project, models' performance and comparison, references used,  check this file called [project-report.pdf](https://github.com/akshayreddykotha/rating-prediction-google-local/blob/master/project-report.pdf). Feel free to write to any of us to discuss any feedback, questions and ideas.

**************************************************************************************************************************
*Trivia*:

A thing I learned with this project about Github is whenever I have to push files larger then 100 MB, Github has this cool application called **Git Large File Storage** - https://git-lfs.github.com/ using which large files are pushed within 3 steps outlined in the link.