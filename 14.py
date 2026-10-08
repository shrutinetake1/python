#14. Longest Common Prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]

        for i in range(len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]

            if len(strs) == 0:
                print("")
        
        return prefix
