import math

class cal(object):

    """
     represents a operations done using calculator
     usage:
     >>>p1=values()
     >>>p2=values(1,2)
     >>>p1.add(p2)
    """
    def __init__(self,operant1,operant2)->None:
        """
         initializing two operants to do operations
         :parm: operant1
         :parm:operant2
         """
        self.operant1=operant1
        self.operant2=operant2
        
##    def move(self,operant1,operant2)->None:
##         self.operant1=operant1
##         self.operant2=operant2
##         
##    def reset(self)->None:
##        """
##          reset the values to 0
##        """
##        self.move(0)

    def add(self)->None:

        return (self.operant1+self.operant2)

value=cal(10,20)
result=value.add()
print(result)



##class calculator:
##    
##    def sum(self,value_1,value_2):
##        sum_result=value_1+value_2
##        return sum_result
##
##
##    def sub(self,value_1,value_2):
##        sub_result=value_1-value_2
##        return sub_result 
##
##    def mul(self,value_1,value_2):
##        mul_result=value_1*value_2
##        return mul_result
##
##obj_1=calculator()
##
##print("sum result{}".format(obj_1.sum(10,20)))
##print("sub result{}".format(obj_1.sub(20,10)))
##print("mul result{}".format(obj_1.mul(10,5)))