#coding:utf-8

from numpy import *
import operator
from array import array



##Giving the training data and the corresponding types
def createDataSet(group, labels):
    retGroup = group
    retLabels = labels
    return retGroup, retLabels

###Sorting by KNN
def kNNclassify(input,dataSet,label,k):
    dataSize = dataSet.shape[0]
    # print "label: "
    # print label
    #Calculate euclidean distance
    diff = tile(input,(dataSize,1)) - dataSet
    # print "diff: "
    # print diff
    sqdiff = diff ** 2
    
    #Adding row vector respectively and then get new row vector. 
    squareDist = sum(sqdiff,axis = 1)
    dist = squareDist ** 0.5
    
    #Sorting the distance
    #Sorting based on the value of elements(greater -> less), return subscript
    sortedDistIndex = argsort(dist)
    # if x = [30, 10, 20, 40]  
    # return numpy.argsort(x) = [1, 2, 0, 3] 
    # print "sortedDistIndex"
    # print sortedDistIndex

    songList = []
    # print "initial songList"
    # print songList

    # ii = 0
    for i in range(0, k):
        
        index = sortedDistIndex[i]
        # songList[ii] =  dist[i]
        # songList.append(label[index])
        songList.append([label[index],dataSet[index]])

        # ii=ii+1
    return songList

    # classCount={}
    # for i in range(k):
    #     voteLabel = label[sortedDistIndex[i]]
    #     #Calculate the number of types that selected K samples belong to
    #     classCount[voteLabel] = classCount.get(voteLabel,0) + 1
    
    # #Choosing the types with the most occurrences
    # maxCount = 0
    # for key,value in classCount.items():
    #     if value > maxCount:
    #         maxCount = value
    #         classes = key

    # return classes 