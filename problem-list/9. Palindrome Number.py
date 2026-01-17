class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = "#".join(str(x))
        i = j = len(str_x) // 2
        while i >= 0 and j < len(str_x) and str_x[i] == str_x[j]:
            i -= 1
            j += 1
        i += 1
        j -= 1

        if i == 0 and j == len(str_x) - 1:
            return True
        return False
