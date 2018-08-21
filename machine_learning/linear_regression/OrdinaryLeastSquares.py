import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
#获取糖尿病的数据集
diabetes = datasets.load_diabetes()
#使用其中的一个特征,np.newaxis的作用是增加维度
diabetes_X = diabetes.data[:,np.newaxis,2]
print(diabetes_X)
#将X变量数据集分割成训练集和测试集
#
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

#将Y目标变量分割成训练集和测试集,
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

#创建线性回归对象
regr = linear_model.LinearRegression()

#使用训练数据来训练模型
regr.fit(diabetes_X_train, diabetes_y_train)

#查看相关系数
print('Coefficients: \n', regr.coef_)
#查看残差平方的均值(mean square error,MSE)
print("Residual sum of squares: %.2f"#%是格式化
      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))

#画出测试的点
plt.scatter(diabetes_X_test,diabetes_y_test,color = 'black')

#画出预测的点
plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue', linewidth=3)
#删除X轴的标度
plt.xticks(())
#删除Y轴的标度
plt.yticks(())
plt.show()