import time


def f(*args):  # create list only with uniqe variables
    list_new = []
    for i in args:
        for y in i:
            if y not in list_new:
                list_new.append(y)
    return list_new


z = list(range(10000))
x = list(range(5000, 15000))
c = (range(10000, 20000))
start = time.time()  # start time counting
f(z, x, c)
stop = time.time() - start  # stop time counting
print(stop)

start2 = time.time()  # start time counting
r = set(z)  # creating set (mnogestvo)
t = r.union(set(x), set(c))  # adding new elements to set (mnogestvo)
stop2 = time.time() - start2  # stop time counting
print(stop2)
