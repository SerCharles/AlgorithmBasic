class Solution(object):
    def get_prefix(self, word):
        prefix = []
        for i in range(len(word)):
            prefix.append(-1)
        k = -1
        for i in range(1, len(word)):
            while k >= 0 and word[k + 1] != word[i]:
                k = prefix[k]
            if word[k + 1] == word[i]:
                k += 1
            prefix[i] = k 
        return prefix 
    
    def kmp(self, main, sub):
        prefix = self.get_prefix(sub)
        k = -1 
        for i in range(len(main)):
            while k >= 0 and sub[k + 1] != main[i]:
                k = prefix[k]
            if sub[k + 1] == main[i]:
                k += 1
                if k == len(sub) - 1:
                    return True 
        return False 
    
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        results = []
        whether = []
        for i in range(len(words)):
            whether.append(False)
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue 
                if self.kmp(words[j], words[i]):
                    whether[i] = True 
        for i in range(len(words)):
            if whether[i] == True: 
                results.append(words[i])
        return results
    