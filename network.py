import pickle
from decimal import Decimal
import math

def sigmoid(n, deriv=False):
	if not deriv:
		return 1 / (1 + Decimal(-n).exp())
	else:
		return Decimal(n).exp()/(1+Decimal(n).exp()) ** 2

def run(picture):
	nodes[0] = picture
	for layer in range(1, len(nodes)):
		for node in range(len(nodes[layer])):
			z = 0
			for i in range(len(nodes[layer-1])):
				z += nodes[layer-1][i] * Decimal(weights[layer][node][i]) + Decimal(biases[layer][node][i])
			nodes[layer][node] = sigmoid(z)
	return nodes[len(nodes)-1]

def get_cost(res, target):
	ideal = [Decimal(1) if i == target else Decimal(0) for i in range(10)]
	c = 0
	for pair in zip(ideal, res):
		c += (pair[0]-pair[1])**2
	return c

def get_gradient(avg_cost):
	layer = 2
	node = 10
	print(weights[layer][node])

global nodes
global weights
global biases
nodes = pickle.load(open('nodes.pk', 'rb'))
weights = pickle.load(open('weights.pk', 'rb'))
biases = pickle.load(open('biases.pk', 'rb'))
data = pickle.load(open('data.pk', 'rb'))

average_cost = 0
for pair in data:
	pic = pair[0]
	num = pair[1]
	result = run(pic)
	cost = get_cost(result, num)
	# print(cost)
	average_cost += cost
average_cost /= len(data)
# print()
print(average_cost)
get_gradient(average_cost)