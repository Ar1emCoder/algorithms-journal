# 1
# summa = 0
# while True:
#     num = int(input())
#     if num <= 0:
#         break
#     summa += num
#
# print(summa)

# 10
# n = int(input())
# summa = 0
# for i in range(n):
#     if i % 3 == 0 or i % 5 == 0:
#         summa += i
#
# print(summa)

# 2
# n = int(input())
# m = int(input())
# for i in range(n, m+1):
#     print(i**2)


# 9
# n = int(input())
# for i in range(n+1):
#     print("*"*i)


# 8
# for i in range(10, -1, -1):
#     print(i, end=" ")


# 7
# n = int(input())
# for i in range(1, n+ 1):
#     if n % i == 0:
#         print(i)


# 6
# arr = []
# while True:
#     s = str(input())
#     if s == "КОНЕЦ":
#         break
#     else:
#         arr.append(s)
# print(arr, sep="\n")


# 3
n = int(input())
cnt = 0
coins = [25, 10, 5, 1]

for coin in coins:
    many = n // coin
    cnt += many
    n %= coin
print(cnt)
