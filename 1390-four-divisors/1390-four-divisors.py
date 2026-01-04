class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for n in nums:
            divisors = set()
            j = 1
            while j * j <= n:
                if n % j == 0:
                    divisors.add(j)
                    divisors.add(n // j)
                j += 1

            if len(divisors) == 4:
                total += sum(divisors)

        return total
