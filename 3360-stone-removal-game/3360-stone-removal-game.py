class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice_turn = True
        for i in range(10, 0, -1):
            if n < i:
                return not alice_turn
            n -= i
            alice_turn = not alice_turn
        return False
