"""
	DBSCAN requires two parameters: ε (eps) and the minimum number of points required to form a dense region[a] (minPts).
	It starts with an arbitrary starting point that has not been visited. This point's ε-neighborhood is retrieved, and if it contains sufficiently many points, a cluster is started.
	Otherwise, the point is labeled as noise. Note that this point might later be found in a sufficiently sized ε-environment of a different point and hence be made part of a cluster.
	If a point is found to be a dense part of a cluster, its ε-neighborhood is also part of that cluster.
	Hence, all points that are found within the ε-neighborhood are added, as is their own ε-neighborhood when they are also dense.
	This process continues until the density-connected cluster is completely found.
	Then, a new unvisited point is retrieved and processed, leading to the discovery of a further cluster or noise.
"""

from sklearn.datasets import load_iris
from math import sqrt, pow

def readData():
	with open("train_set.txt", "r") as f:
		data = f.read()

	data = [l for l in data.split("\n") if l]
	points = []

	for d in data:
		pointX = float(d.split()[0])
		pointY = float(d.split()[1])
		points += [(pointX, pointY)]

	return points

class Point:

	def __init__(self, x = 0, y = 0, vsitedPoint = False, isNoise = False):
		self.x = x
		self.y = y
		self.vsitedPoint = False
		self.isNoise = False

class DBSCAN:

	def __init__(self):
		self.eps = 4
		self.minNumOfPoints = 2
		self.setOfPoints = []
		self.clusters = []
		self.numOfClusers = 0

	def calculateDistance(self, p1, p2):
		px = (p1.x - p2.x)
		py = (p1.y - p2.y)

		return sqrt(pow(px,2) + pow(py,2))

	def regionQuery(self, p):
		pointsInRange = []

		for iS in xrange(len(self.setOfPoints)):
			tempPoint = self.setOfPoints[iS]
			if(self.calculateDistance(p, tempPoint) < self.esp):
				pointsInRange += tempPoint

		return pointsInRange

	def checkIfNeighborhood(self, p):
		isMember = False

		for iC in xrange(len(self.clusters)):
			for jC in xrange(len(self.clusters[iC])):
				if p.x == self.clusters[iC][jC].x and p.y == self.clusters[iC][jC].y:
					isMember = True

		return isMember

	def expandCluster(self, p, neighborPoints):
		self.clusters[self.numOfClusers].append(p)
		iterator = iter(neighborPoints)

		while True:
			try:
				tempNeighbor = iterator.next()
			except StopIteration:
				break
			if not tempNeighbor.vsitedPoint:
				tempNeighbor.vsitedPoint = True
				NeighborPts = self.regionQuery(tempNeighbor)

				if len(NeighborPts) >= self.minNumOfPoints:
					for iN in xrange(len(NeighborPts)):
						neighborPoints += NeighborPts[iN]

			if not self.checkIfNeighborhood(tempNeighbor):
				self.clusters[self.numOfClusers].append(tempNeighbor)

	def DBSCAN(self):
		for iS in xrange(len(self.setOfPoints)):
			tempPts = self.setOfPoints[iS]

			if not tempPts.vsitedPoint:
				tempPts = True
				NeighborPts = self.regionQuery(tempPts)

				if len(NeighborPts) < self.minNumOfPoints:
					tempPts.isNoise = True
				else:
					self.clusters.append([])
					self.numOfClusers += 1
					self.expandCluster(tempPts, NeighborPts)

def main():
	iris = load_iris()["data"]
	# pts = readData()
	print "#pts = {0}".format(len(iris))

	dbscan = DBSCAN()
	dbscan.setOfPoints = iris

	dbscan.DBSCAN()

if __name__ == "__main__":
	main()
