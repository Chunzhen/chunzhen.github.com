#!/usr/bin/env python
# -*- coding:utf-8 -*-

from numpy import *
import operator

#测试函数
def loadDataSet():
	postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
		['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
		['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
		['stop', 'posting', 'stupid', 'worthless', 'garbage'],
		['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
		['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
	classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
	return postingList,classVec

#获取文档集中所有出现的单词
def createVocabList(dataSet):
	vocabSet=set([])      #创建一个空集
	for document in dataSet:
		vocabSet=vocabSet | set(document)    #创建两个集合的并集
	return list(vocabSet)

#返回一个文档中哪些单词是否出现，出现为1，不出现为0，比计算次数
#词集模型
def setOfWords2Vec(vocabList,inputSet):
	returnVec=[0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)]=1
		else:
			print "the word: %s is not in my Vocabulary!" % word
	return returnVec

#返回单词在文档中出现的次数
#词袋模型
def bagOfWords2VecMn(vocabList,inputSet):
	returnVec=[0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)]+=1
	return returnVec

#朴素贝叶斯训练器
#备注右侧代码为原始代码
#备注左侧代码即为修改后的代码，用来处理乘积为0的问题和下溢出问题
def trainNB0(trainMatrix,trainCategory):
	numTrainDocs=len(trainMatrix)
	numWords=len(trainMatrix[0])
	pAbusive=sum(trainCategory)/float(numTrainDocs)
	p0Num=ones(numWords)    #p0Num=zeros(numWords)
	p1Num=ones(numWords)    #p1Num=zeros(numWords)
	p0Denom=2    #p0Denom=0.0
	p1Denom=2    #p1Denom=0.0
	for i in range(numTrainDocs):
		if trainCategory[i]==1:
			p1Num+=trainMatrix[i]
			p1Denom+=sum(trainMatrix[i])
		else:
			p0Num+=trainMatrix[i]
			p0Denom+=sum(trainMatrix[i])
	p1Vect=log(p1Num/p1Denom)#p1Vect=p1Num/p1Denom
	p0Vect=log(p0Num/p0Denom)#p0DVect=p0Num/p0Denom
	return p0Vect,p1Vect,pAbusive

#分类函数吗 vec2Classify为输入测试变量
def classifyNB(vec2Classify,p0Vect,p1Vect,pClass1):
	p1=sum(vec2Classify*p1Vect)+log(pClass1)
	p0=sum(vec2Classify*p0Vect)+log(1-pClass1)
	if p1>p0:
		return 1
	else:
		return 0

def testingNB():
	listOPosts,listClasses=loadDataSet()
	myVocabList=createVocabList(listOPosts)
	trainMat=[]
	for postinDoc in listOPosts:
		trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
	p0V,p1V,pAb=trainNB0(trainMat,listClasses)
	testEntry=['love','my','dalmation']
	thisDoc=array(setOfWords2Vec(myVocabList,testEntry))
	print testEntry, "classified as:",classifyNB(thisDoc,p0V,p1V,pAb)

	testEntry=['stupid','garbage']
	thisDoc=array(setOfWords2Vec(myVocabList,testEntry))
	print testEntry, "classified as:",classifyNB(thisDoc,p0V,p1V,pAb)

#返回小写的词集
def textParse(bigString):
	import re
	listOfTokens=re.split(r'\W*',bigString)
	return [tok.lower() for tok in listOfTokens if len(tok)>2]

def spamTest():
	docList=[]
	classList=[]
	fullText=[]
	for i in range(1,26):
		wordList=textParse(open('email/spam/%d.txt' % i).read())
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(1)
		wordList=textParse(open('email/ham/%d.txt' % i).read())
		docList.append(wordList)
		fullText.extend(wordList)
		classList.append(0)
	vocabList=createVocabList(docList)
	trainingSet=range(50)
	testSet=[]
	for i in range(10):
		randIndex=int(random.uniform(0,len(trainingSet)))
		testSet.append(trainingSet[randIndex])
		del(trainingSet[randIndex])
	trainMat=[]
	trainClasses=[]
	for docIndex in trainingSet:
		trainMat.append(setOfWords2Vec(vocabList,docList[docIndex]))
		trainClasses.append(classList[docIndex])
	p0V,p1V,pSpam=trainNB0(array(trainMat),array(trainClasses))
	errorCount=0
	for docIndex in testSet:
		wordVector=setOfWords2Vec(vocabList,docList[docIndex])
		if(classifyNB(array(wordVector),p0V,p1V,pSpam)!= classList[docIndex]):
			errorCount+=1
	print "the error rate is :%f" % (float(errorCount)/len(testSet))


if __name__=='__main__':
	# listOPosts,listClasses=loadDataSet()
	# myVocabList=createVocabList(listOPosts)
	# trainMat=[]
	# for postinDoc in listOPosts:
	# 	trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
	# p0V,p1V,pAb=trainNB0(trainMat,listClasses)
	# print p0V
	# print p1V
	# print pAb

	#testingNB()

	spamTest()