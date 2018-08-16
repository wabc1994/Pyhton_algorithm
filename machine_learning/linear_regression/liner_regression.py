import numpy as np
import requests

"""
linear regression is the most basic type of regression commonly used for predictive analysis
The idea is simple, we have a data_set and we have a feature's associated with it.
基本思路是：先求梯度下降，计算误差，在运行线性回归 问题，其中线性回归步骤先初始化参数矩阵

权重矩阵由linear regression 初始化，然后梯度下降算法求解，进行跌打，同时进行误差的计算过程
x =n*p , n代表样本数，P代表样本特征的维数，就是多位线性回归 H(X)=B0+ B1X1 + B2X2 + B3X3 +
X =n(p+1) theta： (p+1)*1 权重矩阵 包含 P+1 个，一个偏置值和P个权重值，偏置值放在前面， 后面接权重值,   y =X* theta 运算公式，X和theta 均为向量，y是n*1 
的输出向量
有必要对获得的数据X进行增减列值,  

the right the procedure to implement the gradient descent
Calculate the hypothesis h = X * theta
Calculate the loss = h - y and maybe the squared cost (loss^2)/2m
Calculate the gradient = X' * loss / m
Update the parameters theta = theta - alpha * gradient
"""


"""
in this implement of gradient descent we use y=theta *x ,among which theta is 1*n(n样本数)，while X is n*(p+1) p代表特征位数，在下面的实现中特征维数为1， 
"""
#一元线性回归函数
def collect_dataset():
    """collect data_set from a csv_file
    """
    response = requests.get("https://raw.githubusercontent.com/yashLadha/"+
                            "The_Math_of_Intelligence/master/Week1/ADRvs" +
                            "Rating.csv")
    lines = response.text.splitlines()
    data = []
    for item in lines:
        item = item.split(",")
        data.append(item)
    print("the raw data ", data)
    data.pop(0) #remove the label from the list
    data_set = np.array(data)
    print("data_set.shape", data_set.shape)
    print("data after deal with: ", data_set)
    return data_set



def run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta):
    """
    run the steep gradient descent and updates the feature vector accordingly_
    :param data_x:   contains the data_set
    :param data_y:   contains the output associated with each data_entry
    :param len_data: length of the data_set
    :param alpha:    learning rate of the model
    :param theta:    feature vector(weights for our model)
    :return: update  feature feature's ,using
                     curr_features - alpha_*gradient(w.r.t. feature)
    """
    n = len_data
    #  WE NEED TO transpose data_x into (p+1) *n ,theta is 1*(p+1)
    prod = np.dot(theta, data_x.transpose())

    prod -= data_y
    print("pro: data_x", prod.shape, data_x.shape)
    #prod represent the loss of the hypothesis and true label
    sum_grad = np.dot(prod, data_x)
    print("总梯度的值：",sum_grad.shape)

    # batch-gradient descent
    theta = theta -(alpha / n) * sum_grad
    return theta

def sum_of_square_error(data_x, data_y, len_data, theta):
    """
    this is the cost function
    Return sum of the square error for error calculation
    :param data_x: contains our data_set
    :param data_y: contains the out_put
    :param len_data: len of the data_set
    :param theta: contains the feature vector
    :return: sum of square error computed from given feature
    """
    error  = 0.0
    #prod represent the out_result
    prod = np.dot(theta, data_x.transpose())
    # the error matrix
    prod -= data_y
    #np.square(prod) prod is a 1*n matrix, every_element get square
    sum_elem = np.sum(np.square(prod))
    # np.sum fet sum of the
    error = sum_elem / (2 * len_data)
    return error

def run_linear_regression(data_x, data_y):
    """
    implement linear regression over the data_set
    :param data_x: contain_data
    :param data_y: contains the output(result vector)
    :return      : feature for fine of the best fit (feature vector)
    """
    iteration_s = 100
    alpha = 0.0001550

    no_features = data_x.shape[1]
    len_data = data_x.shape[0]
    print("no_feature :, len_data:   ", no_features , len_data)
    #intinilize the the
    theta  = np.zeros(no_features)
    #iterations how many time do
    for i in range(0,iteration_s):
        theta = run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta)
        error = sum_of_square_error(data_x, data_y, len_data, theta)
        print("at iteration %d - Error is %.5f " % (i+1, error))
    print("theta shape", theta.shape)
    return theta

def main():
    """
    Driver function
    :return:
    """
    data = collect_dataset()
    len_data = data.shape[0]
    data_x =np.c_[np.ones(len_data), data[:,:-1]].astype(float)
    data_y = data[:,-1].astype(float)
    print("data_x: ", data_x)
    print("data_y: ", data_y)
    print("data_x after transpose:", data_x.transpose())
    print("data_y after transpose", data_y.transpose())
    theta = run_linear_regression(data_x, data_y)
    len_result = theta.shape[0]
    print("result feature vector: ")
    for i in  range(0,len_result):
        print("%.5f" % (theta[i]))



if __name__ == "__main__":
    main()