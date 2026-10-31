class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        fin_ans = 0
        for num in nums:
            if num == 1:
                ans += 1
                if ans>fin_ans:
                    fin_ans = ans
            else:
                ans = 0
        return fin_ans