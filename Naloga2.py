import math

def najmanjsi(x):
    return min(x)



def najvecji(x):
    return max(x)


def average(x):
    return sum(x) / len(x)


def nearavg(x):
    average = sum(x)/len(x)
    r = min(x, key=lambda m:abs(m-average))
    return r

y = [4,23,55,7,9]
gha = nearavg(y)
print(gha)