import sys
def intersect(p1,p2):
    answer=[]
    while(len(p1)!=0 or len(p2)!=0):
        a=sys.maxsize
        b=sys.maxsize
        if len(p1)!=0:
            a=p1[0]
        if len(p2) != 0:
            b = p2[0]

        if a==b:
            answer.append(p1.pop(0))
            p2.pop(0)
        elif a<b:
            p1.pop(0)
        else:
            p2.pop(0)
    return answer

def andNot(p1,p2):
    answer=[]
    while(len(p1)!=0 or len(p2)!=0):
        a=sys.maxsize
        b=sys.maxsize
        if len(p1)!=0:
            a=p1[0]
        if len(p2) != 0:
            b = p2[0]

        if a==b:
            p1.pop(0)
            p2.pop(0)
        elif a<b:
            answer.append(p1.pop(0))
        else:
            answer.append(p2.pop(0))
    return answer

def orNot(p1,p2):
    answer=[]
    while(len(p1)!=0 or len(p2)!=0):
        a=sys.maxsize
        b=sys.maxsize
        if len(p1)!=0:
            a=p1[0]
        if len(p2) != 0:
            b = p2[0]

        if a==b:
            p1.pop(0)
            p2.pop(0)
        elif a<b:
            p1.pop(0)
        else:
            p2.pop(0)
    return answer



p1=[2,4,8,16,32,64,128]
p2=[1,2,3,5,8,13,21,34]

#print(intersect(p1,p2))
print(andNot(p1,p2))



def normalized(self):
    magnitude = math.sqrt(self.x ** 2 + self.y ** 2)
    self.x /= magnitude
    self.y /= magnitude
