class Solution:
    def myAtoi(self, s: str) -> int:
        numbers = "0123456789"
        start = 0
        for i in range(len(s)):
            if not s[i] in numbers:
                if s[i] == " ":
                    continue
                elif not s[i] in "+-":
                    return 0 
            start = i
            break
            
            
        no_leading_space = s[start:]
        if len(no_leading_space) == 0:
            return 0
        sign = -1 if no_leading_space[0] == "-" else 1
        if no_leading_space[0] in numbers:
            number = int(no_leading_space[0])
        else:
            number = 0
        for sym in no_leading_space[1:]:
            if sym in numbers:
                number = number * 10 + int(sym)
                if number > (2**31)-1:
                    return -2**31 if sign < 0 else (2**31)-1
            else:
                break
        return sign * number

        
