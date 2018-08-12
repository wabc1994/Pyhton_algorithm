from numpy import *

"""
p(xy)=p(x|y)p(y)=p(y|x)p(x)
p(x|y)=p(y|x)p(x)/p(y)
"""
# 项目案例1 ： 屏蔽社区留言板的不和谐言论

def loadDataSet():
    """
    创建数据集
    :return: 单词列表postingList 所属类别classVec
    """
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],  # [0,0,1,1,1......]
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1] # 1 is abusive, 0 not
    return postingList, classVec

def createVocabList(dataSet):
    """
    获取所有单词的集合
    :param dataSet:  数据集
    :return: 所有单词的集合（即不含重复元素的单词列表）

    """
    vocabSet = set([]) # create empty set
    for doucment in dataSet:
        vocabSet = vocabSet | set(doucment) #union of the two sets
    return list(vocabSet)

dataset, label = loadDataSet()
print(createVocabList(dataset))

def setOfWords2Vec(vocabList,inputSet):
    """
    遍历查看该单词是否出现过，出现该该单词将该单词置1
    :param vocabList: 所有单词集合列表
    :param inputSet: 输入数据集
    :return: 匹配列表[0,1,0,1] 其中1与0表示词汇表中的单词是否出现在输入的数据集中
    """
    #创建一个和词汇表等长的向量，并将其元素都设置为0
    returnVec =[0] * len(vocabList) #[0,0,.....]

    #遍历文档中所有单词，如果出现了词汇表中单词，则将输出的文档向量中的对应值设置为1
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] =1
        else:
            print("the word: %s is not in my vocabulary",word)
    return returnVec



def _trainNB0(trainMatrix, trainCategory):
    """
    训练数据原版
    :param trainMatrix: 文件单词矩阵[[1,0,1,1,1],[],[]]
    :param trainCategory: 文件对应的类别[0,1,1,0],列表长度等于单词矩阵数，其中的1代表对应的文件是侮辱性文件，0代表不是侮辱性文件
    :return:
    """
    #总文件数
    numTrainDocs = len(trainMatrix)
    #总单词数
    numWords = len(trainMatrix[0])
    #侮辱性文件的出现概率
    pAusive  = sum(trainCategory) / float(numTrainDocs)

    #构造单词出现次数列表
    p0Num = zeros(numWords)
    p1Num = zeros(numWords)



    p0Denom = 0.0
    p1Denom = 0.0

    for i in range(numTrainDocs):
        #遍历所有的文件 如果是侮辱性的文件，就计算出此侮辱性文件中出现的单词个数
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom +=sum(trainMatrix[i])
        else:
            #如果不是侮辱性文件，则计算非侮辱性文件中出现的侮辱性单词的个数
            p0Num +=trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    # 类别1，即侮辱性文档的[P(F1|C1),P(F2|C1),P(F3|C1),P(F4|C1),P(F5|C1)....]列表
    # 即 在1类别下，每个单词出现次数的占比
    p1Vect = p1Num / p1Denom  # [1,2,3,5]/90->[1/90,...]
    # 类别0，即正常文档的[P(F1|C0),P(F2|C0),P(F3|C0),P(F4|C0),P(F5|C0)....]列表
    # 即 在0类别下，每个单词出现次数的占比
    p0Vect = p0Num / p0Denom
    return p0Vect,p1Vect,pAusive

def trainNB0(trainMatrix, trainCategory):
    """
    训练数据优化版本
    :param trainMatrix: 文件单词矩阵
    :param trainCategory: 文件对应的类别
    :return:
    """
    # 总文件数
    numTrainDocs = len(trainMatrix)
    # 总单词数
    numWords = len(trainMatrix[0])
    # 侮辱性文件的出现概率
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    # 构造单词出现次数列表
    # p0Num 正常的统计
    # p1Num 侮辱的统计
    # 避免单词列表中的任何一个单词为0，而导致最后的乘积为0，所以将每个单词的出现次数初始化为 1
    p0Num = ones(numWords)  # [0,0......]->[1,1,1,1,1.....]
    p1Num = ones(numWords)

    # 整个数据集单词出现总数，2.0根据样本/实际调查结果调整分母的值（2主要是避免分母为0，当然值可以调整）
    # p0Denom 正常的统计
    # p1Denom 侮辱的统计
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            # 累加辱骂词的频次
            p1Num += trainMatrix[i]
            # 对每篇文章的辱骂的频次 进行统计汇总
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    # 类别1，即侮辱性文档的[log(P(F1|C1)),log(P(F2|C1)),log(P(F3|C1)),log(P(F4|C1)),log(P(F5|C1))....]列表
    p1Vect = log(p1Num / p1Denom)
    # 类别0，即正常文档的[log(P(F1|C0)),log(P(F2|C0)),log(P(F3|C0)),log(P(F4|C0)),log(P(F5|C0))....]列表
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive

def classifyNB(vec2Classify, p0Vec, p1Vec,pClass1):
    """
    使用算法
     # 将乘法转换为加法
        乘法：P(C|F1F2...Fn) = P(F1F2...Fn|C)P(C)/P(F1F2...Fn)
         加法：P(F1|C)*P(F2|C)....P(Fn|C)P(C) -> log(P(F1|C))+log(P(F2|C))+....+log(P(Fn|C))+log(P(C))
    :param vec2Classify:
    :param p0Vec:类别0，即正常文档的[log(P(F1|C0)),log(P(F2|C0)),log(P(F3|C0)),log(P(F4|C0)),log(P(F5|C0))....]列表
    :param p1Vec:类别1，即侮辱性文档的[log(P(F1|C1)),log(P(F2|C1)),log(P(F3|C1)),log(P(F4|C1)),log(P(F5|C1))....]列表
    :param pClass1:类别1 ，侮辱性文件出现的概率
    :return: 类别1 或0
    """
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

def bagOfWords2VecMN(vocabList, input):
    returnVec = [0] * len(vocabList)
    for word in input:
        if word in vocabList:
            returnVec[vocabList.index[word]] +=1
    return returnVec

def testingNB():
    """
    测试朴素贝叶斯算法
    :return:

    """
    #1.加载数据集
    listOPosts, listClasses = loadDataSet()
    #2.创建单词集合

    myVocabList = createVocabList(listOPosts)
    # 3 计算单词是否出现并创建数据矩阵
    trainMat =[]
    for postinDoc in listOPosts:
# 返回m*len(myVocabList)的矩阵， 记录的都是0，1信息
        trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
    # 4.训练数据
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    # 5. 测试数据
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))


if __name__ == '__main__':
    testingNB()