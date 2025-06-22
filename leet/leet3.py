class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d_idx = {}
        p1 = 0
        max_count = 0
        counter = 0
        if s == '':
            return 0
        while p1 != len(s):
            if s[p1] not in d_idx:
                d_idx[s[p1]] = p1
                counter+=1
                p1 += 1
                max_count = max(max_count, counter)
            else:
                p1 = d_idx[s[p1]] + 1
                d_idx = {}
                counter = 0
        return max_count
                