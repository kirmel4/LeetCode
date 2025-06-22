class Solution:
    def findAnagrams(self, s: str, p: str):

        def counter(s):
            string_list = []
            for ch in s:
                string_list.append(ch)

            string_dict = {}
            for ch in string_list:
                if ch not in string_dict:
                    string_dict[ch] = 1
                else:
                    string_dict[ch] = string_dict[ch] + 1

            return string_dict
        id_arr = []
        idx = 0
        c_p = counter(p)
        d = counter(s[idx: idx + len(p)])
        if len(p) > len(s):
            return []
        while idx + len(p)  != len(s)+1  :
            if d == c_p:
                id_arr.append(idx)
            if d[s[idx]] == 1:
                del d[s[idx]]
            else:
                d[s[idx]] -= 1
            idx += 1
            if idx +len(p)-1 == len(s):
                break
            if s[idx +len(p)-1] not in d:
                d[s[idx +len(p)-1]] = 1
            else:
                d[s[idx +len(p)-1]] += 1
                
        return id_arr
            
s = Solution()
print(s.findAnagrams(s = "aaaaaaaaaa", p = "aaaaaaaaaaaaa"))
            
            
            
            