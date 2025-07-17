class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        p = 0
        vowels = set('aeoiu')
        max_count = 0
        curr_count = 0
        while p < k:
            if s[p] in vowels:
                curr_count += 1
            p += 1
        while p < len(s):
            if s[p] in vowels:
                curr_count+=1
            if s[p-k] in vowels:
                curr_count -=1
            max_count = max(curr_count, max_count)
            p+=1               
        print(max_count)
s = Solution()
print(s.maxVowels(s = "abceoadbeiii", k = 4))