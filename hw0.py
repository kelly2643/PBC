
x2 = int(input())
p1 = int(input())
p2 = int(input())
t = int(input())
total_cost = x1*p1 + x2*p2
change = t - total_cost
print(t, total_cost, change, sep=',')
