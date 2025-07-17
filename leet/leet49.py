# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

class Solution:
    def groupAnagrams(self, strs):
        
        d = {}
        
        for str_ in strs:
            
            group = str(sorted(str_))
            
            if group in d:
                d[group].append(str_)
            else:
                d[group] = [str_]
                
        return list(d.values())
        
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        
        