class Solution(object):
    def power(self, times):
        result = 1 
        base = 3
        while times > 0:
            lesser = (times & 0x01)
            if lesser:
                result = result * base 
            base *= 3
            times = (times >> 1)
        return result
    
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        maximum = (2 ** 31) - 1
        times = 0
        while True:
            result = self.power(times)
            if result == n:
                return True 
            if result > n:
                return False 
            if result > (maximum / 3):
                return False
            times += 1