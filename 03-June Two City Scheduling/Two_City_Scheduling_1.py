class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        l1=[]
        for i in costs:
            l1.append(i[0])
        initial = sum(l1)
        extra = [j-i for i,j in costs]
        new = sum(sorted(extra)[:len(costs)//2])
        return initial + new
