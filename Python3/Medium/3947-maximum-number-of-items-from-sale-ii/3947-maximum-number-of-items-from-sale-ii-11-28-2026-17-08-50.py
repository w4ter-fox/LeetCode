class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        for f, _ in items:
            freq[f] += 1

        multiples = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f]:
                multiples[f] = sum(freq[g] for g in range(f, n + 1, f))

        m = min(p for _, p in items)            
        bundles = sorted(
            (p, multiples[f] - 1)
            for f, p in items
            if multiples[f] - 1 > 0 and p < 2 * m
        )

        total = 0
        rem = budget
        for p, d in bundles:                   
            t = min(d, rem // p)
            total += 2 * t
            rem -= t * p
            if t < d:                              
                break

        return total + rem // m            