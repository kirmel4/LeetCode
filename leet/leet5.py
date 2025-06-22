class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(str):
            return str == str[::-1]
        max_l = 0
        max_p = ''
        p1 = 0
        p2 = 0
        while p1 != len(s):
            while p2 != len(s):
                if is_palindrome(s[p1:p2+1]):
                    if len(s[p1:p2+1]) > max_l:
                        max_l = len(s[p1:p2+1])
                        max_p = s[p1:p2+1]
                p2 += 1
            p1+=1
            p2 = p1
        return max_p
            
s = Solution()
print(s.longestPalindrome("cbbd"))
                    