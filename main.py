import cv2
from collections import Counter
from random import shuffle

def create_dataset():
    with open('dataset.txt','w') as f:
        for i in range(0,10):
            for j in range(1,10):
                image = str(i) + '.' + str(j) + '.png'
                pixels = cv2.imread('numbers/'+image).reshape(1,64,3)
                f.write(str(i)+ '::')
                for row in pixels:
                    for col in row:
                        f.write(str(col)+ ',')
                f.write('\n')

create_dataset()

def prediction(sample):
    match_counter = []

    sample = sample.reshape(1,64,3)
    li = []
    for row in sample:
        for col in row:
            li.append(str(col))

    with open('dataset.txt','r') as f:
        dataset = f.readlines()
        for data in dataset:
            number, pixels = data.split('::')
            pixels = pixels.strip(', \n').split(',')

            for i in range(len(pixels)):
                if li[i] == pixels[i]:
                    match_counter.append(number)

    result = Counter(match_counter)
    print("The sample image is very similar to", result.most_common()[0][0])

sample = cv2.imread('sample.png')
prediction(sample)
