class Solution:
    def isThree(self, n: int) -> bool:
        root = math.isqrt(n)
        return root * root == n and self.is_prime(root)
    
    def is_prime(self, num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
        