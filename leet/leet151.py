class Solution:
    def reverseWords(self, s) -> str:
        
        return ' '.join([x for x in s.split() if x != ''][::-1])
s =Solution()
print(s.reverseWords("a good   example"))