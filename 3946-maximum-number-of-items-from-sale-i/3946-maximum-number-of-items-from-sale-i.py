from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        MAX_F = 1500
        freq = [0] * (MAX_F + 1)
        min_price = float('inf')

        for f, p in items:
            freq[f] += 1
            if p < min_price:
                min_price = p

        gain_by_factor = [0] * (MAX_F + 1)
        for f in range(1, MAX_F + 1):
            if freq[f] == 0:
                continue
            total = freq[f]
            for multiple in range(f * 2, MAX_F + 1, f):
                total += freq[multiple]
            gain_by_factor[f] = total

        dp = [-1] * (budget + 1)
        dp[0] = 0

        for f, p in items:
            val = gain_by_factor[f]
            for c in range(budget, p - 1, -1):
                if dp[c - p] != -1:
                    if dp[c - p] + val > dp[c]:
                        dp[c] = dp[c - p] + val

        ans = 0
        for c in range(budget + 1):
            if dp[c] != -1:
                extra = (budget - c) // min_price
                if dp[c] + extra > ans:
                    ans = dp[c] + extra

        return int(ans)