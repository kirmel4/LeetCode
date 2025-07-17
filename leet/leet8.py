class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        res = []

        max_int = 2**31 -1
        min_int = -2**31
        if s == '':
            return 0
        if s[0] == '-':
            res.append('-')
        
        if s[0].isalpha() or s[0] == '.':
            return 0
        
        for i in range(len(s)):

            if s[i].isdigit():
                res.append(s[i])

            elif (s[i].isalpha() or s[i] == '-' or s[i] == '.' or s[i] == '+' or s[i] == ' ') and i > 0:
                
                if len(res) ==0:
                    return 0
                if res[-1].isdigit() and len(res) >0:

                    break
                else:
                    return 0
            
        if res == ['-'] or res ==[]:
            return 0
        
        res = int(''.join(res))
        
        if res < 0:
            return max(res, min_int)
        else:
            return min(res, max_int)
s = Solution()
print(s.myAtoi("-11919730356x"))

            
                