from PIL import Image
import numpy as np

def get_hash(img):
    img = img.resize((100, 100), Image.ANTIALIAS).convert('L')  # 抗锯齿 灰度
    img.save('test.jpg')
    avg = sum(list(img.getdata())) / 10000  # 计算像素平均值
    print(avg)
    s = ''.join(map(lambda i: '0' if i < avg else '1', img.getdata()))  # 每个像素进行比对,大于avg为1,反之为0
    return ''.join(map(lambda j: '%x' % int(s[j:j+4], 2), range(0, 10000, 4)))

def hammingtest(hash1,hash2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2))

def hamming(hash1, hash2, n=20):
    b = False
    # len(hash1) == len(hash2)
    if sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2)) < n:
        b = True
    return b

testlist=[Image.open('1.jpg'),
          Image.open('2.jpg'),
          Image.open('3.jpg'),
          Image.open('4.jpg'),
          Image.open('5.jpg'),
          Image.open('6.jpg'),
          Image.open('7.jpg'),]
hashlist=[]
for x in testlist:
    hashlist.append(get_hash(x))

#for x in hashlist:
#    print(x)
#print(hammingtest(hash1,hash3))

"""
print(hammingtest(hashlist[0], hashlist[1]))
print(hammingtest(hashlist[0], hashlist[2]))
print(hammingtest(hashlist[0], hashlist[3]))
print(hammingtest(hashlist[0], hashlist[4]))
print(hammingtest(hashlist[3], hashlist[4]))
print(hammingtest(hashlist[5], hashlist[6]))
print(hammingtest(hashlist[2], hashlist[5]))
print(hammingtest(hashlist[2], hashlist[6]))
"""

a=get_hash(Image.open('lena_numpy_gray.jpg'))
b=get_hash(Image.open('touxiang.jpg'))
c=get_hash(Image.open('lena_numpy_swap_color.jpg'))
get_hash(testlist[1])
print(c)
print(hammingtest(b,c))
print(hammingtest(hashlist[6],hashlist[5]))
print(hammingtest(hashlist[2],hashlist[0]))
print(hammingtest(hashlist[1],hashlist[0]))
print(hammingtest(hashlist[0],hashlist[4]))
print(hammingtest(hashlist[3],hashlist[4]))