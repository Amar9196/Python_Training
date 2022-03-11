'''
Created on Jul 16, 2019

@author: srilakshmig
'''
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3

times3 = make_multiplier_of(3)
print(times3(4))
print(times3(2)) 

# Multiplier of 5
times5 = make_multiplier_of(5)
print(times5(5)) 
