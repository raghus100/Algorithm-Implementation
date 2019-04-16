res = []
def permutate(soFar, rest):
    if (len(rest) <=0):
        print(soFar+rest)
        res.append((soFar+rest))
        return
    else:
        for i in range(len(rest)):
            rest_string = rest[0:i]+rest[i+1:len(rest)]
            permutate(soFar+rest[i], rest_string)

def permutate_iterate(str):
    count = 0
    for i in range(len(str)):
        for j in range(len(str)):
            tmp = str[0:i]+str[j]+str[i+1:j]+str[i]+str[j+1:len(str)]
            print(tmp)
            count += 1
    print(count)

if __name__ == '__main__':
    str = 'abcd'
#    permutate('',str)
#    print(len(res))
    permutate_iterate(str)
