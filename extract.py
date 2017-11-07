from PIL import Image
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

for n in range(100):
	num = labels[n]
	pic = [i for i in images[:total]]
	im = Image.frombytes('P', (28, 28), bytes(images[:total]))
	im.save(f'extracted_images/pic{n}.png', 'PNG')
	images = images[total:]
	print(n, num)