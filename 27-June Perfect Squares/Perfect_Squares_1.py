class Solution:
    def perfectsquares(self, x):
        list_ps = set()
        for i in range(1, x+1):
            sr = sqrt(i)
            if((sr-floor(sr))==0):
                list_ps.add(i)
        return list_ps
    
    def numSquares(self, n: int) -> int:
        next_dict ={}
        list_ps = self.perfectsquares(n)
        if n in list_ps:
            return 1
        step = 1
        sum_ = 0
        q = list_ps.copy()
        while(len(q)>0):
            step+=1
            new_q = set()
            size = len(q)
            for curr in q:
                for e in list_ps:
                    sum_ = curr + e
                    if(sum_ < n):
                        new_q.add(sum_)
                    if(sum_==n):
                        return step
                size-=1
            q=new_q
        return -1
