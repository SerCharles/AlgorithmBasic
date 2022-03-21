class Solution(object):
    def judge_link(self, source, target):
        length = len(source)
        diff = 0
        for i in range(length):
            if source[i] != target[i]:
                diff += 1
        if diff == 1:
            return True 
        return False
    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        #get begin and end place
        begin_place = -1
        end_place = -1
        for i in range(len(wordList)):
            if wordList[i] == beginWord:
                begin_place = i 
            if wordList[i] == endWord:
                end_place = i 
        if begin_place < 0:
            wordList.append(beginWord)
            begin_place = len(wordList) - 1
        if end_place < 0:
            return 0
        print(begin_place, end_place)
        #build map
        has_link = []
        dist = []
        visit = []
        for i in range(len(wordList)):
            dist.append(14530529)
            visit.append(False)
            link = []
            for j in range(len(wordList)):
                link.append(False)
            has_link.append(link)
        dist[begin_place] = 0
        visit[begin_place] = True
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if i == j:
                    continue 
                has_link[i][j] = self.judge_link(wordList[i], wordList[j])
        for i in range(len(wordList)):
            if has_link[begin_place][i]:
                dist[i] = 1
                
        #dijikstra
        for i in range(len(wordList) - 1):
            min_place = -1
            min_dist = 14530529
            for j in range(len(wordList)):
                #find min
                if visit[j] == False:
                    if dist[j] < min_dist:
                        min_place = j 
                        min_dist = dist[j]

            if min_place < 0:
                break

            for j in range(len(wordList)):
                if visit[j] == False and j != min_place and has_link[min_place][j] == True: 
                    new_dist = dist[min_place] + 1
                    if new_dist < dist[j]:
                        dist[j] = new_dist
            visit[min_place] = True 
        
        if dist[end_place] >= 14530529:
            return 0
        else:
            return dist[end_place] + 1
        
                
            
        