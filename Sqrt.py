class Solution:
    def mySqrt(self, x: int) -> int:
        #heron algorithm
        epsilon=0.000001
        if x>0:
            x_i=x
            x_i_1=1/2*(x_i+(x/x_i))
            while((abs(x_i_1-x_i))>epsilon):
                x_i=x_i_1
                x_i_1=1/2*(x_i+(x/x_i))
                if (abs(x_i_1-x_i)<epsilon):
                    return int(x_i_1)
            return int(x_i_1)
        else:
            return 0


        