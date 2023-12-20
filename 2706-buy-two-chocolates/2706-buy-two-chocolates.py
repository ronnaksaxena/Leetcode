class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first, second = inf, inf
        for n in prices:
            if n < first:
                second = first
                first = n
            elif n < second:
                second = n
        return money - first - second if (first + second) <= money else money
        