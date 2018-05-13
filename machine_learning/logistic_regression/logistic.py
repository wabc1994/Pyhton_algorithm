"""
This program performs two different logistic regression implementations on two
different datasets of the format [float,float,boolean], one
implementation is in this file and one from the sklearn library. The program
then compares the two implementations for how well the can predict the given outcome
for each input tuple in the data_sets.

"""
import math
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import  train_test_split
from numpy import loadtxt,where
from pylab import scatter, show ,legend,xlabel,ylabel

min_max_scaler = preprocessing.MinMaxScaler(feature_range=(-1,1))
df = pd.read_csv("data.csv")


#  get the data from the csv file

#
df.columns = ["grade1","grade2", "label"]
x = df["label"].map(lambda x :float(x.rstrip(";")))
X = df[["grade1","grade2"]]
X = np.array(X)
print(X)
X = min_max_scaler.fit_transform(X)
Y = df["label"].map(lambda x:float(x.rstrip(";")))
Y = np.array(Y)
X_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=1)

# reshape the csv data for use
new_data_csv = pd.DataFrame.from_records(X, columns =["grade1","grade2"])
new_data_csv.insert(2, "label", Y)
new_data_csv.to_csv("clean_data")
log_from_sk = LinearRegression()
log_from_sk.fit(X_train, y_train)
print("the score of sklearn logistic regression model", log_from_sk.score(x_test, y_test))


# model function
def Sigmoid(z):
     G_of_z = float(1.0 / float(1 + np.exp(-1.0 *z)))
     return G_of_z

# x=[feature1 ,feature2] theta =[bo,w1,w2] ,all feature share the whole the parameter value
def  Hypothesis(theta, x):
     z = 0
     for i in range(0,len(theta)):
         z += x[i] * theta[i]
     return Sigmoid(z)

"""
 pi log(q(i)), pi represent the real label value , q(i) represent the model
  hypothesis, so if the logistical regression get two class the if the  m is the number 
  of the sample
"""


def cost_function(X, Y, theta, m):
    """
    损失函数都是迭代加起来的
    :param X: the whole input data_set which contain two feature  m*2 array
    :param Y: the whole sample label data
    :param theta: the weight array contain 1*3
    :param m: the number of the sample
    :return:  return the lost function
    """
    sumofErrors = 0
    for i in range(0,m):
        error = 0
        xi = X[i]
        hi = Hypothesis(theta, xi)
        if Y[i] ==1:
            error = Y[i] * math.log(hi)
        elif Y[i] == 0:
            error = (1-Y[i]) *math.log(1-hi)
        sumofErrors += error
    # get the song
    const = -1/m
    J = const * sumofErrors
    print("cost is ", J)
    return J

## this function create the gradient component for each theta value
## this gradident is the partial derivative by the theta for the current
# for each theta there is a cost function calculated for each member of the dataset

def Cost_function_Derivaitive(X, Y, theta, j, m, alpha):
    """
    get the derivative of the cost function
    :param X: the whole input database
    :param Y:  the whole label
    :param theta: the weight vector
    :param j:
    :param m:
    :param alpha:
    :return: 返回向前迈进的步伐
    """
    sumErrors = 0
    for i in range(0, m):
        xi = X[i]
        xij = xi[j]
        hi = Hypothesis(theta, x[i])
        error = (hi-Y[i]) * xij
        sumErrors += error
    m =len(Y)
    constant = float(alpha/m)
    J = constant * sumErrors
    return J


def Gradient_Descent(X, Y, theta, m , alpha):
    """
    the function use to upgrade the theta vector
    :param X:
    :param Y:
    :param theta:
    :param m:
    :param alpha:
    :return: return the new_theta value
    """
    new_theta = []
    constant = alpha/m
    for j in range(0, len(theta)):
        CFDerivative = Cost_function_Derivaitive(X, Y ,theta, j, m, alpha)
        new_theta_value = theta[j] - CFDerivative
        new_theta.append(new_theta_value)
    return new_theta



def Logistic_Regression(X, Y, alpha, theta, num_iteration):
    """

    :param X:
    :param Y:
    :param alpha:
    :param theta:
    :param num_iters: 迭代的次数，向前跑步的次数
    :return:
    """
    m = len(Y)
    for x in range(0, num_iteration):
        new_theta = Gradient_Descent(X, Y, theta, m, alpha)
        theta = new_theta
        # every 100 iterations value we need to present the value
        if x % 100 == 0:
            cost_function(X, Y, theta, m)
            print("theta: ", theta)
            print("cost is ", cost_function(X, Y, theta, m))
    Declare_winner(theta)


def Declare_winner(theta):
    """

    :param theta:
    :return:
    """
    score = 0
    winner = ""
    scikit_score = log_from_sk.score(x_test, y_test)
    length = len(y_test)
    for i in range(0, x_test):
        prediction =  round(Hypothesis(theta, x_test[i]))
        answer = y_test[i]
        if prediction == answer:
            score += 1
    my_score = float(score / length)
    if my_score > scikit_score:
        print(" you won ")
    elif my_score == scikit_score:
         print("fair play")
    else :
        print("my score: " , my_score)
        print("scikit_score: ",scikit_score)


def main():
    initial_theta = np.zeros(2)
    alpha = 0.1
    iterations = 1000
    Logistic_Regression(X, Y, alpha=alpha, theta=initial_theta,num_iteration=iterations)



if __name__ == "__main__":
    main()


