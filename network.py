import pickle
from collections import defaultdict
import math

def sigmoid(n, deriv=False):
	if not deriv:
		return math.exp(n)/(math.exp(n) + 1)
	else:
		return math.exp(n)/(1+math.exp(n)) ** 2

def run_network(weights, pic):
	nodes[0] = [p/255 for p in pic]
	for layer, layer_weights in weights.items():
		next_layer = defaultdict(int)
		for connection, weight in layer_weights.items():
			next_layer[connection[1]] += nodes[layer][connection[0]]*weight
		nodes[layer+1] = list(map(sigmoid, list(next_layer.values())))
	return nodes

def get_cost(nodes, target):
	ideal = [1 if i == target else 0 for i in range(10)]
	return sum((x-y)**2 for x, y in zip(nodes, ideal))

def get_deriv(nodes, target):
	ideal = [1 if i == target else 0 for i in range(10)]
	for n in range(3, 2, -1):
		print(nodes[n])
		s = 0
		for connection, weight in weights[n-1].items():
			if connection[1] == 0:
				print(connection, weight)
				s += nodes[n-1][connection[0]]*weight
		print(sigmoid(s))


global weights
global nodes
weights = pickle.load(open('weights.pk', 'rb'))
nodes = pickle.load(open('nodes.pk', 'rb'))
data = pickle.load(open('data.pk', 'rb'))

average_cost = 0
for pair in data:
	pic = pair[0]
	target = pair[1]
	nodes = run_network(weights, pic)
	result = nodes[list(nodes.keys())[-1]]
	print(result)
	cost = get_cost(result, target)
	get_deriv(nodes, target)
# 	print(cost)
# 	average_cost += cost
# print('-'*20)
# average_cost /= len(data)
# print(average_cost)