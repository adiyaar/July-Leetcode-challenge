class Solution(object):
    
    def nthUglyNumber(self, n):

        res = []

        res.append(1)

        p2 = 0

        p3 = 0

        p5 = 0

        for i in range(1,n+1):

            minimum = min(res[p2]*2,res[p3]*3,res[p5]*5)

            res.append(minimum)

            if minimum == res[p2]*2:p2+=1

            if minimum == res[p3]*3:p3+=1

            if minimum == res[p5]*5:p5+=1
        
        return res[n-1]
