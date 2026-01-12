class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            missing = target - num
            if missing in seen:
                return [seen.get(missing), i]
            seen.update({num: i})
        return []
            

            
