class Solution(object):
    def subtractProductAndSum(self, n):
        product=1
        sum1=0
        while n>0:
            product = product*(n%10)
            sum1=sum1+(n%10)
            n=n//10
        return product-sum1