# Third attempt ~ beat 55%
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        count = count_1 = count_2 = current = last = 0
        len_1 = len(nums1)
        len_2 = len(nums2)
        total_length = len_1 + len_2
        index_to_find = int(total_length/2)
        even = True if total_length % 2 == 0 else False
        # print(index_to_find, even)
        while count <= index_to_find:
            if count_1 < len_1 and count_2 < len_2:
                if nums1[count_1] < nums2[count_2]:
                    last = current
                    current = nums1[count_1]
                    count_1 += 1
                else:
                    last = current
                    current = nums2[count_2]
                    count_2 += 1
            elif count_1 < len_1:
                last = current
                current = nums1[count_1]
                count_1 += 1
            else:
                last = current
                current = nums2[count_2]
                count_2 += 1 
            count += 1
        if even:
            return (last + current)/2
        return current
# Second attempt ~ beat 33%
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         nums1.extend(nums2)
#         result = sorted(nums1)
#         len_result = len(result)
#         med_i = int(len_result/2) 
#         if len_result % 2 == 0:
#             return (result[med_i] + result[med_i-1])/2
#         return result[med_i]
# First attempt ~ beat 5%
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
                
