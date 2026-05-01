class Solution:
    def calPoints(self, operations: List[str]) -> int:
        tally = []
        def is_integer(s):
            try:
                int(s)
                return True
            except ValueError:
                return False

        for o in operations:
            if is_integer(o):
                tally.append(int(o))
            
            elif o == "+":
                tally.append(tally[-1] + tally[-2])
                              
            elif o == "D":
                tally.append(tally[-1] * 2)
            
            elif o == "C":
                tally.pop()
        
        output = 0
        for t in tally:
            output = output + t
        
        return output
