
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import itertools

        nums = [str(i) for i in range(1, n + 1)]
        permutations = itertools.permutations(nums)

        for i, p in enumerate(permutations, 1):
            if i == k:
                return ''.join(p)

        