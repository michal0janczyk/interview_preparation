"""
    In pattern recognition, the k-nearest neighbors algorithm (k-NN) is a non-parametric method used for classification and regression.
    In both cases, the input consists of the k closest training examples in the feature space. The output depends on whether k-NN is used for classification or regression:
    In k-NN classification, the output is a class membership. An object is classified by a majority vote of its neighbors,
    with the object being assigned to the class most common among its k nearest neighbors (k is a positive integer, typically small). If k = 1,
    then the object is simply assigned to the class of that single nearest neighbor.
    In k-NN regression, the output is the property value for the object. This value is the average of the values of its k nearest neighbors.
    k-NN is a type of instance-based learning, or lazy learning, where the function is only approximated locally and all computation is deferred until classification.
    The k-NN algorithm is among the simplest of all machine learning algorithms.
"""

import copy
from sklearn.datasets import load_iris
import heapq
import math
import numpy as np
import random
import operator

pSplit = 0.5
pK = 3

def calculateDistance(p1, p2):
    assert len(p1) == len(p2)
    distance = 0.0

    for iN in xrange(len(p1)):
        distance += pow((p1[iN] - p2[iN]), 2)

    return math.sqrt(distance)

def findNeighbors(trainingSet, p0, k):
    possibleNeighbours = []

    for iT in xrange(len(trainingSet)):
        dist = calculateDistance(p0, trainingSet[iT][0])
        elem = (dist, trainingSet[iT][1])

        possibleNeighbours += [elem]

    possibleNeighbours.sort(key = lambda t: t[0])
    neighbors = []

    for iN in xrange(k):
        neighbors += [possibleNeighbours[iN][1]]

    assert len(neighbors) == k
    return neighbors

def findNeighbors2(trainingSet, p0, k):
    kNeighbors = []

    for iT in xrange(len(trainingSet)):
        dist = calculateDistance(p0, trainingSet[iT][0])
        elem = (dist, trainingSet[iT][1])

        if len(kNeighbors) < k:
            kNeighbors += [elem]
        else:
            val = max(kNeighbors, key = lambda t: t[0])

            if elem[0] < val[0]:
                iMax = kNeighbors.index(val)
                kNeighbors[iMax] = elem

    assert len(kNeighbors) == k
    return [t[1] for t in kNeighbors]

def findNeighbors3(trainingSet, p0, k):
    kNeighbors = []

    for iT in xrange(len(trainingSet)):
        dist = calculateDistance(p0, trainingSet[iT][0])
        elem = ((-1) * dist, trainingSet[iT][1])

        if len(kNeighbors) < k  :
            heapq.heappush(kNeighbors, elem)
        elif elem[0] > kNeighbors[0][0]:
            heapq.heappop(kNeighbors)
            heapq.heappush(kNeighbors, elem)

    assert len(kNeighbors) == k
    return [t[1] for t in kNeighbors]

def classify(neighbors, classes, maxClass):
    classCounts = []

    for c in xrange(maxClass + 1):
        classCounts += [0]

    for iN in neighbors:
        curClass = classes[iN]
        classCounts[curClass] += 1

    maxC = classCounts.index(max(classCounts))
    return maxC

def main():
    iris = load_iris()["data"]
    classes = load_iris()["target"]

    print "#pts = {0}".format(len(iris))

    trainingSet = []
    testSet = []

    for iP in xrange(len(iris)):
        if random.random() < pSplit:
            trainingSet += [(iris[iP], iP)]
        else:
            testSet += [iris[iP]]

    print 'Train set: ' + str(len(trainingSet))
    print 'Test set: ' + str(len(testSet))

    predictions = []
    for iS in xrange(len(testSet)):
        neighbors = findNeighbors3(trainingSet, testSet[iS], pK)
        result = classify(neighbors, classes, 2)

        predictions.append(result)
        print "predicted = {0} point = {1}".format(result, testSet[iS])

if __name__ == "__main__":
    main()
