import numpy as np

class PoissonMLE(object):

	'''
	python class to compute poisson regression coefficients and
	standard errors via maximum likelihood estimation. The MLE
	is found either via simple gradient descent (unstable) 
	or via iteratively reweighted least squares. The latter 
	algorithm follows the description in "PPMLHDFE: Fast Poisson 
	Estimation withHigh-Dimensional Fixed Effects" by Sergio Correia,
	Paulo Guimaraes, and Tom Zylkin.

	inputs
	- y: m x 1 numpy-array [target variable]
	- X: m x (p+1) numpy-array [p predictors plus 1 constant]

	(c) 2020 Sebastian Hohmann
	'''

	def __init__(self, y, X):
		self.y = y
		self.X = X

	def compute_gradient(self, theta):
		grad = -self.X.T @ (self.y - np.exp(self.X @ theta))
		return grad

	def gradient_descent(self, theta_init, learning_rate, tol=10e-6, max_iter=100, verbose=True):
		diff = 10
		theta0 = theta_init
		it = 0
		while diff > tol and it < max_iter:
			it+=1
			theta1 = theta0 - learning_rate * self.compute_gradient(theta0)
			diff = np.sum( np.square( theta0 - theta1 ))
			theta0 = theta1
		self.theta = theta1

	def compute_cov(self):
		hess = self.X.T @ np.diag(np.exp(self.X @ self.theta).reshape(-1)) @ self.X
		self.covmat = np.linalg.inv(hess)

	def irls(self, tol=10e-8, max_iter=100):

		'''
		compute theta_MLE via iteratively reweighted least squares
		see https://arxiv.org/pdf/1903.01690v2.pdf for the algorithm 
		and https://gtools.readthedocs.io/en/latest/usage/gpoisson/index.html for the deviance
		'''

		mu = (self.y + self.y.mean()) / 2
		z = np.log(mu) + (self.y - mu) / mu
		W = np.diag(mu.reshape(-1))

		dev0 = np.zeros(self.y.shape)
		dev0[self.y!= 0] = 2 * (np.log(self.y[self.y!=0] / mu[self.y!=0]) - (self.y[self.y!=0] - mu[self.y!=0]))

		devdiff = 1
		it = 0

		while devdiff > tol and it < max_iter:

			theta = np.linalg.inv( (self.X.T @ W @ self.X ) ) @ ( self.X.T @ W @ z )

			mu = np.exp(self.X @ theta)
			W = np.diag(mu.reshape(-1))
			z = self.X @ theta + (self.y - mu) / mu

			dev1 = np.zeros(self.y.shape)
			dev1[self.y!= 0] = 2 * (np.log(self.y[self.y!=0] / mu[self.y!=0]) - (self.y[self.y!=0] - mu[self.y!=0]))

			devdiff = np.max( np.abs(dev1 - dev0) / (dev0 + 1) )
			dev0 = dev1
			it += 1

		self.theta = theta











