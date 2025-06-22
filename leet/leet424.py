class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        r = 0
        max_len = 0
        if len(s) == 1:
            return 1
        while l != len(s) - 1:
            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]] += 1
            max_count = max(list(d.values()))
            if r - l +1 - max_count > k:
                d[s[l]] -= 1
                d[s[r]] -= 1
                l += 1
            else:
                max_len = max(max_len, r- l +1 )
                if r < len(s) - 1:
                        r += 1
                else:
                    break                
        return max_len
s = Solution()
print(s.characterReplacement("A", k = 1))
             