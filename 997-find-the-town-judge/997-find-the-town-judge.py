class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if len(trust) == 0:
            if n == 1:
                return 1
            else:
                return -1
        '''
        foundNodes = []
        for i in range(len(trust)):
            if trust[i][0] not in foundNodes:
                foundNodes.append(trust[i][0])
            if trust[i][1] not in foundNodes:
                foundNodes.append(trust[i][1])
        '''
        nodes = {j:0 for j in range(1,n+1)}
        found = {}
        for x in range(len(trust)):
            nodes[trust[x][0]] += 1
            if trust[x][1] in found:
                found[trust[x][1]] += 1
            else:
                found[trust[x][1]] = 1
        
        print(nodes, found)
        
        for y in nodes.keys():
            if nodes[y] == 0 and y in found and found[y] == n-1:
                return y
            
        return -1
    
