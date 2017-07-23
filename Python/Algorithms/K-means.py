"""
	k-means clustering is a method of vector quantization, originally from signal processing, that is popular for cluster analysis in data mining.
	k-means clustering aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean, serving as a prototype of the cluster.
	This results in a partitioning of the data space into Voronoi cells.
	The problem is computationally difficult (NP-hard); however, there are efficient heuristic algorithms that are commonly employed and converge quickly to a local optimum.
	These are usually similar to the expectation-maximization algorithm for mixtures of Gaussian distributions via an iterative refinement approach employed by both algorithms.
	Additionally, they both use cluster centers to model the data; however, k-means clustering tends to find clusters of comparable spatial extent,
	while the expectation-maximization mechanism allows clusters to have different shapes.
	The algorithm has a loose relationship to the k-nearest neighbor classifier, a popular machine learning technique for classification that is often confused 
	with k-means because of the k in the name. One can apply the 1-nearest neighbor classifier on the cluster centers obtained by k-means to classify new data into the existing clusters.
	This is known as nearest centroid classifier or Rocchio algorithm.
"""

from scipy.spatial import distance
import copy
import numpy as np
import random

import matplotlib.pyplot as plt

def redData():

	with open("train_set.txt", "r") as f:
		data = f.read()

	data = [l for l in data.split("\n") if l]
	points = []
	X = []
	Y = []

	for d in data:
		pointX = float(d.split()[0])
		pointY = float(d.split()[1])
		points += [(pointX, pointY)]


	return points

def distanceDiff(p1, p2):
    assert len(p1) == len(p2)
    diff = 0.0

    for iP in xrange(len(p1)):
        diff += distance.euclidean(p1[iP], p2[iP]) ** 2

    return diff

def computeCenters(k, clusters, points):
    assert len(clusters) == len(points)
    nDims = len(points[0])

    centroid = [0.0 for _ in xrange(nDims)]
    centroids = [copy.deepcopy(centroid) for _ in xrange(k)]

    for i in xrange(len(points)):
        for d in xrange(nDims):
            centroids[clusters[i]][d] += points[i][d]

    for iK in xrange(k):
        nPoints = len([i for i in clusters if i == iK])

        if nPoints == 0:
            continue

        for d in xrange(nDims):
            centroids[iK][d] /= nPoints

    return centroids

def closestCentroid(point, centroids):
    minDistance = float('inf')
    belongsToCluster = None

    for i in xrange(len(centroids)):
        centroid = centroids[i]
        dist = distance.euclidean(point, centroid)

        if dist < minDistance:
            minDistance = dist
            belongsToCluster = i

    return belongsToCluster

def genCentroids(k, points):
    minVals, maxVals = [], []
    nDims = len(points[0])

    for d in xrange(nDims):
        vals = [points[i][d] for i in xrange(len(points))]
        minVals += [min(vals)]
        maxVals += [max(vals)]

    centroids = []

    for iK in xrange(k):
        c = []

        for iD in xrange(nDims):
            val = random.uniform(minVals[iD], maxVals[iD])
            c += [val]

        centroids += [c]

    return centroids

def evalCentroids(centroids, points, clusters):
    assert len(points) == len(clusters)

    err = 0.0 # Main measure
    k = len(centroids)

    for iK in xrange(k):
        curErr = 0.0 # Error for the current cluster
        curPoints = [points[iP] for iP in xrange(len(points)) if clusters[iP] == iK]

        for p in curPoints:
            curErr += distanceDiff(p, centroids[iK])
        err += curErr

    return err / float(k)

def kMeans(k, points, nTries = 30):
    bestClusters, bestCentroids = None, None

    for i in xrange(nTries):
        iIter = 1
        finish = False

        centroids = genCentroids(k, points)

        while not finish:
            finish = True

            clusters = [closestCentroid(points[i], centroids) for i in xrange(len(points))]
            newCentroids = computeCenters(k, clusters, points)

            # Are new centroids different from old?
            for iC in xrange(len(centroids)):
                if centroids[iC] != newCentroids[iC]:
                    finish = False

            centroids = newCentroids
            iIter += 1

        if bestCentroids is None:
            bestClusters = clusters
            bestCentroids = centroids
        else:
            err1 = evalCentroids(centroids, points, clusters)
            err2 = evalCentroids(bestCentroids, points, bestClusters)

            print "#iter = {0}, err = {1} / {2}".format(iIter, err1, err2)

            if err1 < err2:
                bestClusters = clusters
                bestCentroids = centroids

    return bestClusters, bestCentroids

def main():
    k = 3

    pkt = redData()
    clusters, centroids = kMeans(k, pkt)

    plt.scatter([p[0] for p in pkt], [p[1] for p in pkt])
    plt.scatter([p[0] for p in centroids], [p[1] for p in centroids], color='red')

    plt.show()

    print centroids
    print clusters

if __name__ == "__main__":
	main()
