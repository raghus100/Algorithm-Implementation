def permutate(soFar, rest):
    if (len(rest) <=1):
        print(soFar+rest)
        return
    else:
        for i in range(len(rest)):
            rest_string = rest[0:i]+rest[i+1:len(rest)]
            permutate(soFar+rest[i], rest_string)

if __name__ == '__main__':
    str = 'abcd'
    permutate('',str)