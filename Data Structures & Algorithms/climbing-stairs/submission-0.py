class Solution:
    def climbStairs(self, n: int) -> int:
        ways = {1: 1, 2: 2}

        def distinct_ways(x):
            if x in ways:
                return ways[x]

            else:
                ways[x] = distinct_ways(x-1) + distinct_ways(x-2)
                return ways[x]

        return distinct_ways(n)        