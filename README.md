# About

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]

This application provides an overview of the dataset that provides messages that contain labels of spam and ham.

The app involved the best machine learning model chosen from the notebook that will then be deployed in Streamlit.

The dataset was provided from this [source](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset). 

In the notebook, you can see the following:
- Libraries/Dependencies
- EDA (Exploratory Data Analysis)
- Data Pre-processing
- Model Building and Evaluation
- Saving of Model

The prediction is made regarding spam and ham messages utilizing a chosen trained machine learning model.

The dataset is stored as csv files inside the data directory. In order to check the code, go through the Datasets directory in this repository. 
# Model Definition

The structure of training the model is to wrap the process around a scikit-learn pipeline, there were about 10 models trained in the notebook and only 1 of them is chosen to be used for deployment of Streamlit so that messages can be classified if it is spam or ham (non-spam).

Models:

- Multinomial NB
- Random Forest
- K Neighbors
- SVC
- Logistic Regression
- XGB
- Decision Tree
- AdaBoost
- Extra Trees
- Gradient Boosting

The model used for the streamlit is Extra Trees with an accuracy of 98.37%, I'm planning to utilize cross validation and random search for hyperparameter tuning in the future.
# Run the App

To run locally, clone the repository, go to the directory and install the requirements.

```
pip install -r requirements.txt
```

Next, go to the src directory and then run:

```
streamlit run app.py
```