import random
import pickle
nodes = {}
weights = {}
biases = {}
node_counts = [784, 16, 16, 10]
for n, c in enumerate(node_counts):
	nodes[n] = [0]*c

for n in range(1, len(node_counts)):
	weights[n] = {}
	biases[n] = {}
	for i in range(len(nodes[n])):
		weights[n][i] = [0]*len(nodes[n-1])
		biases[n][i] = [0]*len(nodes[n-1])
		for j in range(len(nodes[n-1])):
			weights[n][i][j] = random.uniform(-4, 4)
			biases[n][i][j] = random.uniform(-1, 1)

with open('nodes.pk', 'wb') as p:
	pickle.dump(nodes, p)
with open('weights.pk', 'wb') as p:
	pickle.dump(weights, p)
with open('biases.pk', 'wb') as p:
	pickle.dump(biases, p)