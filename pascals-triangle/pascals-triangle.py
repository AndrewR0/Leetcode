class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #tri = [[1]*(numRows) for _ in range(numRows)]
        tri = [[1]]
        for r in range(1,numRows):
            tri.append([1]*(r+1))
            for c in range(1,r):
                #print(r,c)
                tri[r][c] = tri[r-1][c] + tri[r-1][c-1]
                #print(tri)
        return tri