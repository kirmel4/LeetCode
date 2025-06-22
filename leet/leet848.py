class Solution:
    def shiftingLetters(self, s: str, shifts) -> str:
        # for i, shift in enumerate(shifts):
        #     for j in range(i+1):
                
        #         new_ord =  (ord(new_str[j]) -ord('a') +shift%26 )%26 + ord('a')
        #         new_str[j] = chr(new_ord)
        new_str = ['']*len(s)
        cum_shift = 0
        for i in range(len(shifts) - 1, -1, -1):
            cum_shift += shifts[i]
            new_str[i] = chr((ord(s[i]) - ord('a') + cum_shift%26)%26 + ord('a'))
        return ''.join(new_str)
s = Solution()
print(s.shiftingLetters( s = "aaa", shifts = [1, 2,3 ]))
            
        