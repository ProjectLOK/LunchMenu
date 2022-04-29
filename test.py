fibo = [None]*60
fibo[0] = 0
fibo[1] = 1

n = int(input())
for i in range(50):
    fibo[i + 2] = fibo[i] + fibo[i + 1]

print(fibo[n])