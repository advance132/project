#找出10000以内的完美数。
import math
for n in range (2,10000):
    sum = 1
    for i in range (2,int(math.sqrt(n)+1)):
        if n%i==0:
            sum+=i
            if n//i!=i and n%i==0:
                sum+=n//i
    if sum == n:
        print(n)