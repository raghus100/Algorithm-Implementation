class Solution:
    res = []
    def permutate(self, soFar, rest):
        if (len(rest) <=0):
            print(soFar+rest)
            self.res.append((soFar+rest))
            return
        else:
            for i in range(len(rest)):
                rest_string = rest[0:i]+rest[i+1:len(rest)]
                self.permutate(soFar+rest[i], rest_string)

    def permutate_iterate(self, str):
        count = 0
        for i in range(len(str)):
            for j in range(len(str)):
                tmp = str[0:i]+str[j]+str[i+1:j]+str[i]+str[j+1:len(str)]
                print(tmp)
                count += 1
        print(count)

    def permutation(self, rest, so_far):
        if not rest:
            print(so_far)
            return
        for i, j in enumerate(rest):
            remain = rest[0:i] + rest[i+1:len(rest)]
            self.permutation(remain, so_far + [j])


    def getPermutation(self, n: int, k: int) -> str:
        in_list = list(range(1, n+1))
        so_far = []
        self.permutation(in_list, [])

if __name__ == '__main__':
    str = 'abcd'
    sol = Solution()
   # sol.permutate('', str)
   #print(len(sol.res))
   # sol.permutate_iterate(str)
    sol.getPermutation(3, 3)
