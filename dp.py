class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        results = []
        for i in range(m + 1):
            result = []
            for j in range(n + 1):
                result.append(0)
            results.append(result)
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    results[i][j] = max(results[i - 1][j], results[i][j - 1], results[i - 1][j - 1] + 1)
                else: 
                    results[i][j] = max(results[i - 1][j], results[i][j - 1])
        return results[m][n]
                    