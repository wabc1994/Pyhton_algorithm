import numpy
"""
implementation of gradient descent algorithm for minimizing cost fo a linear hypothesis function
"""
import numpy as np
train_data = ( ((5,2,3),15), ((6,5,9),25), ((11,12,13),41), ((1,1,1),8), ((11,12,13),41))
test_data = ( ((515,22,13),555), ((61,35,49),150))
parameter_vector = [2, 4, 1, 5]
m = len(train_data)
LEARNING_RATE = 0.009


X_train = []
y_train = []
def get_data(data_input_tuple):
    for i in range(0, len(data_input_tuple)):
        X_train.append(data_input_tuple[i][0])
        y_train.append(data_input_tuple[i][1])

X_train = np.array(X_train)
y_train = np.array(y_train)

def _error(example_no, data_set="train"):
    """

    :param example_no: train_data or test data
    :param data_set: example number whose error has to be checked
    :return: error in example
    """
    return calculate_hypothesis_value(example_no, data_set)-output(example_no,data_set)

def _hypothesis_value(data_input_tuple):
    """
    calculates hypothesis function value for a given input
    :param data_input_tuple: input tuple for a particular example
    :return: value of hypothesis function at that point
    """
    hyp_val = 0
    for i in range(len(parameter_vector)-1):
        hyp_val += data_input_tuple[i] *parameter_vector[i+1] # add the calculate
    hyp_val += parameter_vector[0]  #  add bias value
    return hyp_val

def output(example_no, data_set):
    """

    :param example_no: test data_train_data
    :param data_set:  example whose output is to be fetched
    :return: output for that example
    """
    if data_set == "train":
        return train_data[example_no][1]
    elif data_set == "test":
        return test_data[example_no][1]

def calculate_hypothesis_value(example_no, data_set):
    """
    calculates the hypothesis_value for a given example
    :param example_no:  test_data or train_data
    :param data_set:  example whose hypothesis value is to be calculated
    :return: hypothesis_value for that example
    """
    if data_set == "train":
        return _hypothesis_value(train_data[example_no][0])
    elif data_set =="test":
        return _hypothesis_value(test_data[example_no][0])

def summation_of_cost_derivation(index, end=m):
    """
    calculate the sum of cost function derivative
    :param index:  index wrt derivative is being calculated
    :param end:  value where summation ends ,default is m, number of example
    :return: returns the summation of cost derivative
    """
    summation_value = 0
    for i  in range(end):
        if index ==-1:
            summation_value += _error(i)
        else:
            summation_value += _error(i)*train_data[i][0][index]
    return summation_value

def get_cost_derivative(index):
    """
    :param index: index of the parameter vector wrt or derivatives is to be calculated
    :return: derivative writ to that index
    """
    cost_derivative_value = summation_of_cost_derivation(index, m)/m
    return cost_derivative_value

def run_gradient_descent():
    global parameter_vector
    absolute_error_limit =0.000002
    relative_error_limit =0

    # while true classical style
    j = 0
    while True:
        j +=1
        temp_parameter_vector = [0,0,0,0]
        for i in range(0, len(parameter_vector)):
            cost_derivative = get_cost_derivative(i-1)
            temp_parameter_vector[i] = parameter_vector[i] - LEARNING_RATE * cost_derivative
         #get out of the whole while
        if np.allclose(parameter_vector,temp_parameter_vector,atol=absolute_error_limit, rtol=relative_error_limit):
            break
        parameter_vector =temp_parameter_vector
    print("number of iterations : ", j)
    print("the final parameter_vector" ,parameter_vector)

def test_gradient_descent():
    for i in range(len(test_data)):
        print("actual output: ", output(i,"test"))
        print("hypothesis output: ",calculate_hypothesis_value(i,"test"))


if __name__ == "__main__":
    run_gradient_descent()
    test_gradient_descent()