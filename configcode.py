from configparser import ConfigParser
config=ConfigParser()
config.read('config.cfg')
def getid():
    k=config.get('section1','id')
    k=int(k)+1
    print(k)
    config.set('section1','id',str(k))
    num=config.get('section1','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
def getid1():
    k=config.get('section2','id')
    k=int(k)+1
    print(k)
    config.set('section2','id',str(k))
    num=config.get('section2','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
#create task ids
def getid2():
    k=config.get('section3','id')
    k=int(k)+1
    print(k)
    config.set('section3','id',str(k))
    num=config.get('section3','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
def getid3():
    k=config.get('section4','id')
    k=int(k)+1
    print(k)
    config.set('section4','id',str(k))
    num=config.get('section4','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
def getid4():
    k=config.get('section5','id')
    k=int(k)+1
    print(k)
    config.set('section5','id',str(k))
    num=config.get('section5','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
def getid5():
    k=config.get('section6','id')
    k=int(k)+1
    print(k)
    config.set('section6','id',str(k))
    num=config.get('section6','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
#creates ids for transactions in fp
def getid6():
    k=config.get('section7','id')
    k=int(k)+1
    print(k)
    config.set('section7','id',str(k))
    num=config.get('section7','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
def getid7():
    k=config.get('section8','id')
    k=int(k)+1
    print(k)
    config.set('section8','id',str(k))
    num=config.get('section8','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
def getid8():
    k=config.get('section9','id')
    k=int(k)+1
    print(k)
    config.set('section9','id',str(k))
    num=config.get('section9','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
#make website id's for Picta S.A
def getid9():
    k=config.get('section10','id')
    k=int(k)+1
    print(k)
    config.set('section10','id',str(k))
    num=config.get('section10','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
#make webpage ids for Picta S.A
def getid10():
    k=config.get('section11','id')
    k=int(k)+1
    print(k)
    config.set('section11','id',str(k))
    num=config.get('section11','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
#make ids for adds in Pict A.P
def getid11():
    k=config.get('section12','id')
    k=int(k)+1
    print(k)
    config.set('section12','id',str(k))
    num=config.get('section12','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
#make ids for promocodes in Picta A.P
def getid12():
    k=config.get('section13','id')
    k=int(k)+1
    print(k)
    config.set('section13','id',str(k))
    num=config.get('section13','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
#ids for activations in picta a.p
def getid13():
    k=config.get('section14','id')
    k=int(k)+1
    print(k)
    config.set('section14','id',str(k))
    num=config.get('section14','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
#token ids for picta a.p
def getid14():
    k=config.get('section15','id')
    k=int(k)+1
    print(k)
    config.set('section15','id',str(k))
    num=config.get('section15','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
# Myaccount model ids for picta ap
def getid15():
    k=config.get('section16','id')
    k=int(k)+1
    print(k)
    config.set('section16','id',str(k))
    num=config.get('section16','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
def getid16():
    k=config.get('section17','id')
    k=int(k)+1
    print(k)
    config.set('section17','id',str(k))
    num=config.get('section17','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num
# ids for listadd model in picta a.p
def getid17():
    k=config.get('section18','id')
    k=int(k)+1
    print(k)
    config.set('section18','id',str(k))
    num=config.get('section18','id')
    with open('config.cfg','w') as f:
        config.write(f)
    return num