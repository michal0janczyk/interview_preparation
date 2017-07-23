"""
    MSE or mean squared deviation (MSD) of an estimator (of a procedure for estimating an unobserved quantity) measures the average of the squares of the errors or deviations—that is,
    the difference between the estimator and what is estimated. MSE is a risk function, corresponding to the expected value of the squared error loss or quadratic loss.
    The difference occurs because of randomness or because the estimator doesn't account for information that could produce a more accurate estimate.
    The MSE is a measure of the quality of an estimator—it is always non-negative, and values closer to zero are better.
    The MSE is the second moment (about the origin) of the error, and thus incorporates both the variance of the estimator and its bias.
    For an unbiased estimator, the MSE is the variance of the estimator. Like the variance, MSE has the same units of measurement as the square of the quantity being estimated.
    In an analogy to standard deviation, taking the square root of MSE yields the root-mean-square error or root-mean-square deviation (RMSE or RMSD),
    which has the same units as the quantity being estimated; for an unbiased estimator, the RMSE is the square root of the variance, known as the standard deviation.
"""

import random

def mse(a, b, points):
    err = 0.0

    for p in points:
        fx = a * p[0] + b

        curErr = (fx - p[1]) ** 2
        err += curErr

    return err / float(len(points))

def opti(points):
    pop = [(random.uniform(-100, 100), random.uniform(-100, 100)) for _ in xrange(100)]
    fits = [mse(pop[i][0], pop[i][1], points) for i in xrange(len(pop))]

    for iIter in xrange(50):
        pass

    iBest = None

    for iF in xrange(len(fits)):
        if iBest is None or fits[iF] < fits[iBest]:
            iBest = iF

    return pop[iBest]

def gradient(points):
    a = random.uniform(-100, 100)
    b = random.uniform(-100, 100)



with open("train_set.txt", "r") as f:
    data = f.read()

data = [l for l in data.split("\n") if l]
points = []

for d in data:
    pointX = float(d.split()[0])
    pointY = float(d.split()[1])

    points += [(pointX, pointY)]

res = opti(points)
print res
