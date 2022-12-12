import random

def kuraCek():
    alan = []
    veren = []
    with open('isimler.txt','r',encoding='utf-8') as isimler:
        isimler.seek(0)
        for i in isimler.readlines():
            i = i.split('\n')
            alan.append(i[0])
            veren.append(i[0])

    random.shuffle(veren)
    sonuc = list(zip(alan,veren))

    for i in sonuc:
        if i[0] == i[1]:
            return kuraCek()

    return sonuc

for i in (kuraCek()):
    print(i)