from PIL import Image
import pickle
labels = open('train-labels.idx1-ubyte', 'rb').read()
images = open('train-images.idx3-ubyte', 'rb').read()

lmagic = int(labels[:4].hex(), 16)
imagic = int(images[:4].hex(), 16)
llen = int(labels[4:8].hex(), 16)
ilen = int(images[4:8].hex(), 16)
nrow = int(images[8:12].hex(), 16)
ncol = int(images[12:16].hex(), 16)
total = nrow*ncol

if lmagic != 2049 or imagic != 2051 or llen != ilen:
	print('corrupted filetype or non-matching labels and images')
	quit()

length = ilen

labels = labels[8:]
images = images[16:]

data = []

for n in range(1):
	num = labels[n]
	pic = [i for i in images[n*total:(n+1)*total]]
	data.append((pic, num))
with open('data.pk', 'wb+') as f:
	pickle.dump(data, f)