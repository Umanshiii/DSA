#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in m:
                m[key] = []

            m[key].append(word)

        return list(m.values())
