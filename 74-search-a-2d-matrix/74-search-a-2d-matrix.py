class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        left = 0
        right = len(matrix[0])-1
        
        for i in range(len(matrix)):
            if target == matrix[i][left]:
                return True
            elif target == matrix[i][right]:
                return True
            elif target > matrix[len(matrix)-1][right]:
                return False
            elif target > matrix[i][right]:
                start = i+1
            elif target < matrix[i][right]:
                break
        print(start)
        
        while left < right:
            
            mid = (left + right)//2
            
            if matrix[start][mid] == target:
                return True
            elif matrix[start][mid] < target and mid != left:
                left = mid
            elif matrix[start][mid] > target and mid != right:
                right = mid
            else:
                break
        return False