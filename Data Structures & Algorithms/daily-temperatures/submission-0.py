class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waiting = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                stk_i = stack.pop()
                waiting[stk_i] = index - stk_i
            
            stack.append(index)

        
        return waiting