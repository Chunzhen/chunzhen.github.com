#!/usr/bin/env python
# -*- coding:utf-8 -*-
from numpy import *
import operator
import os

def classifyKNN(inX,dataset,labels,k):
	datasetSize=dataset.shape[0]
	diffMat=tile(inX,(datasetSize,1))-dataset
	sqDiffMat=diffMat**2
	sqDistances=sqDiffMat.sum(axis=1) #同行各列相加操作
	distances=sqDistances**0.5
	sortedDistIndicies=distances.argsort()
	classCount={}
	for i in range(k):
		voteIlabel=labels[sortedDistIndicies[i]]
		classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
	sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]

def createDataSet():
	group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels=['A','A','B','B']
	return group,labels

def file2matrix(filename):
	fr=open(filename)
	arrayOLines=fr.readlines()
	numberOfLines=len(arrayOLines)
	returnMat=zeros((numberOfLines,3))
	classLabelVector=[]
	index=0
	labels={'largeDoses':3,'smallDoses':2,'didntLike':1}
	for line in arrayOLines:
		line=line.strip()
		listFromLine=line.split('\t')
		returnMat[index,:]=listFromLine[0:3]
		classLabelVector.append(labels[listFromLine[-1]])
		index+=1
	return returnMat,classLabelVector

def autoNorm(dataset):
	minVals=dataset.min(0)
	maxVals=dataset.max(0)
	ranges=maxVals-minVals
	normDataSet=zeros(shape(dataset))
	m=dataset.shape[0]
	normDataSet=dataset-tile(minVals,(m,1))
	normDataSet=normDataSet/tile(ranges,(m,1))
	return normDataSet,ranges,minVals

def datingClassTest():
	hoRatio=0.1
	datingDataMat,datingLabels=file2matrix('datingTestSet.txt')
	normDataSet,ranges,minVals=autoNorm(datingDataMat)
	m=normDataSet.shape[0]
	numTestVecs=int(m*hoRatio)
	errorCount=0
	for i in range(numTestVecs):
		classifierResult=classifyKNN(normDataSet[i,:],normDataSet[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
		print "the classifier came back with:%d, the real answer is: %d" % (classifierResult,datingLabels[i])
		if(classifierResult!=datingLabels[i]):
			errorCount+=1
	print errorCount
	print "the total accuracy is:%f" % (1-float(errorCount)/float(numTestVecs))


import matplotlib
import matplotlib.pyplot as plt
def plot(datingDataMat):
	print datingDataMat[0:20]
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15*array(datingLabels),5*array(datingLabels))
	plt.show()

def img2vector(filename):
	returnVect=zeros((1,1024))
	fr=open(filename)
	for i in range(32):
		lineStr=fr.readline()
		for j in range(32):
			returnVect[0,32*i+j]=int(lineStr[j])
	return returnVect

def handwritingClassTest():
	hwLables=[]
	trainingFileList=os.listdir('digits/trainingDigits')
	m=len(trainingFileList)
	trainingMat=zeros((m,1024))
	for i in range(m):
		fileNameStr=trainingFileList[i]
		fileStr=fileNameStr.split('.')[0]
		classNumber=int(fileStr.split('_')[0])
		hwLables.append(classNumber)
		trainingMat[i,:]=img2vector('digits/trainingDigits/%s' % fileNameStr)

	testFileList=os.listdir('digits/testDigits')
	errorCount=0
	mTest=len(testFileList)
	for i in range(mTest):
		fileName=testFileList[i]
		fileStr=fileName.split('.')[0]
		classNumberStr=int(fileStr.split('_')[0])
		vectorUnderTest=img2vector('digits/testDigits/%s' % fileName)
		classifierResult=classifyKNN(vectorUnderTest,trainingMat,hwLables,3)
		print "the classifier came back with:%d, the real answer is: %d" % (classifierResult,classNumberStr)
		if(classifierResult!=classNumberStr):
			errorCount+=1

	print "errorCount:%d" % errorCount
	print "error rate:%f" % (errorCount/float(mTest))

if __name__=='__main__':
	#datingDataMat,datingLabels=file2matrix('datingTestSet.txt')
	#print datingLabels[0:20]
	#plot(datingDataMat)
	
	#datingClassTest()

	#testVector=img2vector('digits/testDigits/0_13.txt')
	#print testVector

	handwritingClassTest()
