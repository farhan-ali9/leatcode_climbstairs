class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr={}
        arr[1]=1
        arr[2]=2
        def climb(n):
            if n in arr:
                return arr[n]
            else:
                arr[n]=climb(n-1)+climb(n-2)
                return arr[n]
        return climb(n)
             
            
