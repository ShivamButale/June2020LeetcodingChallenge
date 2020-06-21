class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k-=1
        l=list(range(1,n+1))
        o=''
        for p in range(n):
            f=int(math.factorial(n-p-1))
            x, k = k//f, k%f
            o+=str(l[x])
            l.remove(l[x])
        return o
