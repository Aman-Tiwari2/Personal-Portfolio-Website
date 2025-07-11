'''# To visualize the data into python matplotlib




# To show the academic performance on graph using year and percentage 

years = [2020, 2021, 2022, 2023, 2024]
marks = [80, 67, 83, 69.9, 71.9]

# To add the given dataset into graph

plt.plot(years, marks)

# To set the graph title 

plt.title("Academic Performance Graph")

# To set the label of y and x axiss
plt.xlabel("Years")
plt.ylabel("Marks")

# To display the graph 
plt.show()'''

# Write a program to display data using random distribution upto 1 lakh  and range 0,9



'''xaxis = np.random.randint(0,100000, 100)
yaxis = np.arange(1,100000, 1000)
plt.scatter(xaxis,yaxis)

plt.show()'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats # To use in linear regression 
from sklearn.metrics import r2_score # To use in polynomial regression




# Create a graph for pawan girlfriend list

years = [2012, 2013, 2014, 2015, 2016, 2017, 2018]
number_of_girlfriend = [1,0,0,0,2,3,0]

'''plt.plot(years,number_of_girlfriend)

plt.show()'''

# To predict the future girlfriend for pawan sir's 

# Linear regression will help to predict the future data when the data transform in linear way 

# To calculate the slope and intercept and std erro and co-relation coefficient using linear regression

slope, intercept, r, p, std_error = stats.linregress(years, number_of_girlfriend)
print(r)

# Note:  If r is nearby 1 or -1 (best_prediction) use linear regression 
# Note: If r is nearby 0 (worst prediction) use polynomial 


# To predict the future the data using function of linear regression 

def predict_gf(x):
    return slope * x + intercept

# To predict the future girlfriend's list

future_gf = predict_gf(2025)
print(future_gf)

# To Draw the dataset into graph 

'''plt.plot(years, number_of_girlfriend)
plt.show()'''

# To calculate the prediction using polynomial model and dataset 

polynomialModel = np.poly1d(np.polyfit(years, number_of_girlfriend, 3))

# To calculate the future data

future_gf = polynomialModel(2025)
print(future_gf)


# When we need to find prediction in yes/no(bool) it comes under classification model 
# Area of use in classification -
# Weather forcasting
# Stock market prediction
# Elections
# Job selection 
# Match winning
# Fraud detection 