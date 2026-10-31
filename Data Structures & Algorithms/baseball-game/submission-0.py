class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for num in operations: 
            if num == "+":
                addscore = ans[-1]+ans[-2]
                ans.append(addscore)
            elif num == "C":
                ans.pop()
            elif num == "D":
                double = ans[-1]*2
                ans.append(double)
            else: 
                ans.append(int(num))
        return sum(ans)
            
