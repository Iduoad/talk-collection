from sys import argv, exit

def extract(filename):
    rf=open(filename,'r')
    counter=0
    d={}
    for line in rf:
        if counter == 2 :
            break
        if "---\n" in line:
            counter+=1
            continue
        #print(line.split(':',1))
        if ':' in line:
            key=line.split(':',1)[0].strip()
            value=line.split(':',1)[1].strip()
            d[key]=value
    return d

def key_exists(d,key):
    value = d.get(key)
    if value is None or value == '' or value.isspace():
        return False
    return True

def validate(d):
    keys = ['title', 'type', 'description', 'source', 'tags']
    for key in keys:
        if key_exists(d,key) == False:
            return False
    if not (key_exists(d,'author') or key_exists(d,'speaker') or key_exists(d,'instructor')):
        return False
    return True

if __name__ == "__main__":
    if len(argv) > 1:
        for filename in argv[1:]:
            if not validate(extract(filename)):
                exit(1)

    exit(0)
