class Solution:
    def addBinary(self, a, b):
        x = int(a, 2)
        y = int(b, 2)

        return bin(x + y)[2:]
                