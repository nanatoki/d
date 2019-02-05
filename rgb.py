from PIL import Image
import math
import operator
from functools import reduce
"""
def calc_Hist(img):
    w,h = img.size
    pix = img.load()
    calcR = [0 for i in range(0,256)]
    calcG = [0 for i in range(0,256)]
    calcB = [0 for i in range(0,256)]
    for i in range(0,w):
        for j in range(0,h):
            (r,g,b) = pix[i,j]
            #print (r,g,b)
            calcR[r] += 1
            calcG[g] += 1
            calcB[b] += 1
    calcG.extend(calcB)
    calcR.extend(calcG)

    calc = [0 for i in range(0,96)]
    step = 0
    start = 0
    while step < 96:
        for i in range(start,start+8):
            calc[step] += calcR[i]
        start = start+8
        step += 1
    #print calc
    return calc

def compare(h1,h2):
    result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    return result
"""
def compare2(img,img2):
    image1 = img.resize((100, 100), Image.ANTIALIAS).convert('L')
    image2 = img2.resize((100, 100), Image.ANTIALIAS).convert('L')
    h1 = image1.histogram()
    h2 = image2.histogram()
    result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    print(result)
    return result

testlist=['1.jpg',
          '2.jpg',
          '3.jpg',
          '4.jpg',
          '5.jpg',
          '6.jpg',
          '7.jpg',
          '8.jpg',
          '9.jpg',
          '10.jpg',
          '11.jpg',
          '12.jpg',
          ]
resultlist=[0,]
for x in range(1,12):
    resultlist.append(compare2(Image.open(testlist[0]),Image.open(testlist[x])))

d={}
d.update(zip(testlist,resultlist))
print(d)

answer=sorted(d.items(),key=lambda item:item[1])
print("\nThe most similar:")
for x in answer:
    print(x)
