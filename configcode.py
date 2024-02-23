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