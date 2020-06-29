class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def helper(i):
            while(len(dictionary[i])>0):
                helper(dictionary[i].pop(0))
            least.insert(0, i)
        
        dictionary = defaultdict(list)
        for i, j in tickets:
            dictionary[i].append(j)
            dictionary[i].sort()
        least = []
        helper("JFK")
        return least
