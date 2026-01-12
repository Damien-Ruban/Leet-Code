# First attempt
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         result = []
#         count = 0
#         count_2 = 0

#         for num1 in nums1:
#             for num2 in nums2[count_2:]:
#                 if num1 > num2:
#                     result.append(num2)
#                     count_2 += 1
#                 else:
#                     break
#             result.append(num1)
#         result.extend(nums2[count_2:])
#         med_i = int(len(result)/2)
#         if len(result) % 2 == 0:
#             return (result[med_i] + result[med_i-1])/2
#         return result[med_i]
                
