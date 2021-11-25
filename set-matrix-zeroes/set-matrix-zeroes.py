class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        dic = {}
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    x = f'{i},{j}'
                    dic[x] = j
                    
        #print(list(dic.keys()))
        for k in list(dic.keys()):
            #print(k.split(','))
            k = k.split(',')
            matrix[int(k[0])] = [0]*len(matrix[int(k[0])])
            for l in range(len(matrix)):
                #print(k, k[2])
                matrix[l][int(k[1])] = 0
                    