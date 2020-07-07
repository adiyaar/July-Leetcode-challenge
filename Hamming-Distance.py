class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum([z == '1' for z in bin(x ^ y)][2:])
        
