###K-�����㷨����

![knn](knn.png)

k-�����㷨���ò�����ͬ����ֵ֮��ľ��뷽�����з���
```
�ŵ㣺���ȸߡ����쳣ֵ�����С������������趨
ȱ�㣺���㸴�Ӷȸߡ��ռ临�Ӷȸ�
�������ݷ�Χ����ֵ�ͺͱ����
```
ԭ������һ���������ݼ��ϣ���Ϊѵ����������������������ÿ�����ݶ����ڱ�ǩ��������֪����������ÿһ��������������Ķ�Ӧ��ϵ������û�б�ǩ�������ݺ󣬽������ݵ�ÿ�������������������ݶ�Ӧ���������бȽϣ�Ȼ���㷨��ȡ���������������������ݣ�����ڣ��ķ����ǩ������ֻѡ���������ݼ���ǰk�������Ƶ����ݣ������k-�����㷨��k�ĳ�����ͨ��k�ǲ�����20��������
####k-�����㷨��һ������
1. �ռ����ݣ�����ʹ���κη���
2. ׼�����ݣ������������Ҫ����ֵ������ǽṹ�������ݸ�ʽ
3. �������ݣ�����ʹ���κη���
4. ѵ�����ݣ�k-�����㷨����Ҫѵ��
5. �����㷨����������ʣ�׼ȷ�ʣ�
6. ʹ���㷨�������������ݺͽṹ����������������k-�����㷨�ж��������ݷֱ������ĸ�����

#####k-�����㷨α���룺
* ��δ֪��������ݼ��е�ÿ����ִ�����²�����
* ������֪������ݼ��еĵ��뵱ǰ��֮��ľ��룻
* ���վ��������������
* ѡȡ�뵱ǰ�������С��k���㣻
* ȷ��ǰk�������������ֵ�Ƶ�ʣ�
* ����ǰk�������Ƶ����ߵ������Ϊ��ǰ���Ԥ�����

#####�ؼ����룺
```
def classifyKNN(inX,dataset,labels,k):
     datasetSize=dataset.shape[0]
     diffMat=tile(inX,(datasetSize,1))-dataset
     sqDiffMat=diffMat**2
     sqDistances=sqDiffMat.sum(axis=1) #ͬ�и�����Ӳ���
     distances=sqDistances**0.5
     sortedDistIndicies=distances.argsort()
     classCount={}
     for i in range(k):
          voteIlabel=labels[sortedDistIndicies[i]]
          classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
     sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
     return sortedClassCount[0][0]
```
����`numpy`��`tile`�����ú�ѧϰһ�£�[Numpy��tile���� ](http://blog.csdn.net/qinning199/article/details/26158289)

�ڼ�����������֮��ľ���ʱ������ŷʽ���룬���������ľ��롣

####��һ������ֵ��
```
def autoNorm(dataset):
     minVals=dataset.min(0)
     maxVals=dataset.max(0)
     ranges=maxVals-minVals
     normDataSet=zeros(shape(dataset))
     m=dataset.shape[0]
     normDataSet=dataset-tile(minVals,(m,1))
     normDataSet=normDataSet/tile(ranges,(m,1))
     return normDataSet,ranges,minVals
```

#####���������Լ����վ�Ĳ��Դ��룺
```
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
```

2015-10-13 by Chunzhen