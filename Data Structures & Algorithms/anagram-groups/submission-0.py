class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_anagram = {}
        for s in strs:
            s_sorted = sorted(s)
            s_key = ''.join(s_sorted)
            if s_key not in seen_anagram:
                seen_anagram[s_key] = []
        
            seen_anagram[s_key].append(s)

        final : List[str] = list(seen_anagram.values())
        return final      
