class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        path = []
        res = []
        visited = set()

        def backtrack(curr : int) : 
            
            if curr == 0 : 
                new_path = path[:]
                new_path.sort()
                key = tuple(new_path)
                if key not in visited : 
                    visited.add(key)
                    res.append(new_path)
                return 
            
            if curr < 0 : 
                return 

            for j in range(n) : 
                if nums[j] <= curr : 
                    path.append(nums[j])
                    backtrack(curr - nums[j])
                    path.pop()

                
        backtrack(target)

        return res 