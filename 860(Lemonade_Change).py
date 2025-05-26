class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        n=len(bills)
        five=0
        ten=0
        for i in range(0,n):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                if five>=1:
                    five-=1
                    ten+=1
                else:
                    return False
            else:
                if five>=1 and ten>=1:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True
        