# find coin combinations that sum up to A
import copy
def isSubarray(coins, A, S):
    if (len(coins) <=0 and A !=0) or A < 0: return None
    elif A == 0:
        print S
        return 1
    else:
        isSubarray(coins[1:], A, S)
	Sn = copy.copy(S)
	Sn.append(coins[0])
        isSubarray(coins[1:], A-coins[0], Sn)

        
if __name__ == '__main__':
    l = [1,2,5,6, 9, 10]
    isSubarray(l, 11, [])
