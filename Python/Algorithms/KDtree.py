"""
    The k-d tree is a binary tree in which every node is a k-dimensional point.
    Every non-leaf node can be thought of as implicitly generating a splitting hyperplane that divides the space into two parts, known as half-spaces.
    Points to the left of this hyperplane are represented by the left subtree of that node and points right of the hyperplane are represented by the right subtree.
    The hyperplane direction is chosen in the following way: every node in the tree is associated with one of the k-dimensions, with the hyperplane perpendicular to that dimension's axis.
    So, for example, if for a particular split the "x" axis is chosen, all points in the subtree with a smaller "x" value than
    the node will appear in the left subtree and all points with larger "x" value will be in the right subtree.
    In such a case, the hyperplane would be set by the x-value of the point, and its normal would be the unit x-axis
"""

class Node:
    def __init__(self, val, left, right, par):
        self.val = val
        self.left = left
        self.right = right
        self.par = par

def construct(points, dim):
    if len(points) == 0:
        return None

    nDims = len(points[0])
    assert len([p for p in points if len(p) == nDims]) == len(points)

    node = Node()

    points = list(points)
    points.sort(key = lambda p: p[dim])

    iMid = len(points) / 2
    midPoint = points[iMid]

    node.val = midPoint

    nextDim = dim + 1
    if nextDim == nDims:
        nextDim = 0

    node.left = construct(points[ : iMid], nextDim)
    node.right = construct(points[iMid + 1 : ], nextDim)

    return node

def main():
    root = construct(points, 0)
