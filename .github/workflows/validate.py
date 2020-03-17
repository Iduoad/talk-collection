import pprint

def get_elements(string):
    key = string.split(':',1)
    return key

def get_dict(filename):
    with open(filename) as ff:
        headers = ff.readlines()
        indices = [i for i, x in enumerate(headers) if x == "---\n"]
        d = {}
        if len(indices) < 2:
            return d

        content = headers[indices[0] + 1 : indices[1]]

        for line in content:
            d[get_elements(line)[0]] = get_elements(line)[1]

        return d
if __name__ == '__main__':
    filename = 'git-intermediate-techniques.md'
    pprint.pprint(get_dict(filename))

