class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        moneyLeft = income
        taxAmt = 0.0
        for i, (bound, percent) in enumerate(brackets):
            quantity = bound - (brackets[i-1][0] if i > 0 else 0)
            # Ran out of money
            if moneyLeft < quantity:
                taxAmt += (moneyLeft * (percent/100.0))
                moneyLeft = 0
            else:
                # Have enough money
                taxAmt += (quantity * (percent/100.0))
                moneyLeft -= quantity
            # Done taxing
            if moneyLeft == 0:
                break
            # Last bracket
            if i == len(brackets) - 1 and moneyLeft > 0:
                taxAmt += (moneyLeft * (percent/100.0))
                moneyLeft = 0
        return taxAmt
                           
                
                
            
        