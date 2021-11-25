class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dic = {}
        
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        dic = sorted(dic.items(), key = lambda x:x[1])
        print(dic)
        i = len(dic)-1
        while k > 0: 
            print(dic[i])
            ans.append(dic[i][0])
            
            i -= 1
            k -= 1
        return ans
            