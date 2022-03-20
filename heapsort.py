class Solution(object):
    def min_heapify(self, heap, start_index):
        if start_index >= len(heap):
            return
        l = start_index * 2
        r = start_index * 2 + 1
        pivot = start_index 
        if l < len(heap) and heap[pivot] > heap[l]:
            pivot = l
        if r < len(heap) and heap[pivot] > heap[r]:
            pivot = r 
        if pivot != start_index:
            temp = heap[start_index]
            heap[start_index] = heap[pivot]
            heap[pivot] = temp 
            self.min_heapify(heap, pivot)
    
    def heapsort(self, heap):
        result = []
        while(len(heap) > 1):
            mini = heap[1]
            temp = heap[len(heap) - 1]
            heap[len(heap) - 1] = heap[1]
            heap[1] = temp
            heap.pop(len(heap) - 1)
            result.append(mini)
            self.min_heapify(heap, 1)
        return result
    
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        nums.insert(0, 0)
        half = length // 2
        for j in range(1, half + 1):
            i = half + 1 - j
            self.min_heapify(nums, i)
        sort = self.heapsort(nums)
        print(sort)
        result = []
        for i in range(length):
            if sort[i] == target:
                result.append(i)
        return result
        