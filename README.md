# Summary rating-prediction-google-local
Predict ratings of google local reviews in order to better recommend the places to users based on historical data and the sentiment within the reviews.

**Data Source**: https://cseweb.ucsd.edu/~jmcauley/datasets.html#google_local
**In collaboration with**: [Shiyi Hua](https://www.linkedin.com/in/shiyi-letty-hua-2a7117129/), [Ziyuan Yan](https://www.linkedin.com/in/ziyuan-esther-yan-664732132/)

**Data dictionary**: The source link provides a good sense of what are all the fields we have.
**Visualization**: Though this is not a project which heavily depends on exploratory analysis and visualizations, we  have some basic visualizations and the code in [visualization.Rmd](). You can also have a quick glance of what they are in the detailed [report]().
**Models**:
Trivial baseline: model-00
Bag-of-words in Ridge regression: model-01
Bag-of-words in Ridge regression + hour + price level + review length: model-02. There are various variations of models with different encodings like one-hot, categorical encoding of price level and hour.
Bag-of-words 

For a detailed report of the entire project,the models performance, referenes used check this file called [project-report.pdf](). Feel free to write to any of us to discuss any feedback, questions and ideas.
