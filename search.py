from operator import itemgetter
from math import sqrt
import csv

def reader(add='ratings.csv'):
    with open(add, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # ヘッダーを読み飛ばしたい時

        ratings={}
        for x in range(1,611):
            ratings[str(x)]={}

        for row in reader:
            d1 = {row[1]: eval(row[2])}
            ratings[row[0]].update(d1)

        return ratings

def readerName(id,add='movies.csv'):
    with open(add, 'r') as db01:
        reader = csv.DictReader(db01)
        for row in reader:
            if row['movieId'] == id:
                #print(row)
                return(row['title'])


def get_pearson(data, person1, person2):
    item_list = []
    [item_list.append(item) for item in data[person1] if item in data[person2]]
    n = len(item_list)
    if n < 1: return 0

    ave_1 = sum([data[person1][item] for item in item_list]) / n
    ave_2 = sum([data[person2][item] for item in item_list]) / n

    top = sum([(data[person1][item] - ave_1) * (data[person2][item] - ave_2) for item in item_list])
    under = sqrt(sum([pow(data[person1][item] - ave_1, 2)for item in item_list])) * sqrt(sum([pow(data[person2][item] - ave_2, 2)for item in item_list]))
    if under == 0: return 0
    return top / under

def get_similar_list(data, me):
    person_list = {}
    for person in data:
        if person == me: continue
        person_list[person] = get_pearson(data, me, person)

    return sorted(person_list.items(), key = itemgetter(1), reverse = True)

def advise(data,me):
    a_sim = get_similar_list(data, str(me))
    temp={}
    for x in range(0, 3):
        temp.update(data[a_sim[x][0]])
    temp=sorted(temp.items(), key=itemgetter(1), reverse=True)
    result=[]
    for x in range(0,5):
        result.append(readerName(temp[x][0]))
    print("Recommended for people like userId= "+str(me)+" :\n")
    for x in result:
        print(x)


data = reader()
advise(data,1)