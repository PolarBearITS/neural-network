import random
from decimal import Decimal
import pickle
acc = 100
weights = {}
nodes = {}
node_counts = [784, 16, 16, 10]
for n, c in enumerate(node_counts):
	nodes[n] = [0]*c
for n, c in enumerate(node_counts[:-1]):
	layer = {}
	for i in range(c):
		for j in range(node_counts[n+1]):
			w = random.randrange(-4*acc, 4*acc)/acc
			layer[(i, j)] = w
	weights[n] = layer
with open('weights.pk', 'wb+') as f:
	pickle.dump(weights, f)
with open('nodes.pk', 'wb+') as f:
	pickle.dump(nodes, f)