class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        s = sorted(people, key=lambda x: (-x[0], x[1]))
        #print("S = ", s)
        for i in range(len(s)):
            s.insert(s[i][1], s.pop(i))
        #print("S = ", s)
        return s
