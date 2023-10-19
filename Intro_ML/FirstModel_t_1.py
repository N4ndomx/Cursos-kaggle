import pandas as pd

melbourne_file_path = 'melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
pd=melbourne_data.columns
print(pd)
# The Melbourne data has some missing values (some houses for which some variables weren't recorded.)
# We'll learn to handle missing values in a later tutorial.  
# Your Iowa data doesn't have missing values in the columns you use. 
# So we will take the simplest option for now, and drop houses from our data. 
# Don't worry about this much for now, though the code is:

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)
#Selecting The Prediction Target
y = melbourne_data.Price
#Choosing "Features"
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
#By convention, this data is called X.
X = melbourne_data[melbourne_features]
#review the data we'll be using to predict house prices using the describe method and the head method, which show
print(X.describe())

print(X.head())

#Visually checking your data with these commands is an important part of a data scientist's job. 
#You'll frequently find surprises in the dataset that deserve further inspection.


#Building Your Model
#use the scikit-learn library to create your models. When coding, this library is written as sklearn, as you will see in the sample code. Scikit-learn is easily the most popular library for modeling

#Define: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.
#Fit: Capture patterns from provided data. This is the heart of modeling.
#Predict: Just what it sounds like
#Evaluate: Determine how accurate the model's pre

from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1) #random_state ensures you get the same results in each run. This is considered a good practice.


# Fit model
melbourne_model.fit(X, y)
#
#print("Making predictions for the following 5 houses:")
#print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))

print(y.head)
