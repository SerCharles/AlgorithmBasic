class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        solution = 0
        multiply = 1
        while num > 0:
            lesser = num & 0x01
            if lesser == 0:
                solution += multiply
            multiply = multiply << 1
            num = num >> 1
        return solution
    