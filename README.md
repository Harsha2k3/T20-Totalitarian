# T20 Totalitarian: Mastering Score Predictions

---

## Project Description and Workflow

The T20 World Cup Score Prediction project aims to predict the total runs scored by a team in a T20 cricket match using the XGBoost algorithm. XGBoost is a popular machine learning algorithm used for predictive modeling.

#### The workflow for the T20 World Cup Score Prediction project is as follows:

- **Data Collection:** Collect data on past T20 cricket matches, including the team playing, runs scored, wickets taken, overs bowled, and other relevant information. This data can be sourced from various cricket databases, APIs, or websites.     
  [DataSet Link](https://www.kaggle.com/datasets/veeralakrishna/cricsheet-a-retrosheet-for-cricket)

- **Data Preprocessing:** Clean and preprocess the data to ensure that it is consistent and accurate. This can involve tasks such as removing missing values, handling categorical variables, and feature engineering.

- **Feature Selection:** Identify the most relevant features for the prediction model. This can be done using techniques such as correlation analysis, feature importance ranking, and domain knowledge.

- **Model Training:** Train a Linear Regression, Random Forest Regression and XGBRegression models using the preprocessed data and the selected features. The XBGRegressor gives the maximum R2 Score.So, we choose XGBRegressor as main model.The XGBoost model is a gradient boosting algorithm that uses decision trees as base learners.

- **Model Evaluation:** Evaluate the performance of the XGBoost model using metrics such as mean absolute error, mean squared error, and R-squared.

- **Prediction:** Use the trained and optimized XGBoost model to predict the total runs scored by a team in a T20 cricket match based on the relevant features.

- **Deployment:** Deploy the XGBoost model as a web application on Herokuapp.

## Website Overview:-
Check the model by clicking on the below link  
For better Expereince adjust the screen size to 67%
### [T20 Score Predictor](https://t20-score-275ae826d4e8.herokuapp.com)

#### Developed By :
- Manne Girish Chowdary
- Vali Sai Yaswanth Reddy
- Mamidipaka Sriharsha
- Tummala Nikhil Phaneendra
