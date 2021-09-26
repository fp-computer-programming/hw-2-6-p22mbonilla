# Author MB 09/26/2021

a = input("how many free shots where made")
b  = input("how many inside shots where made")
c  = input("how many outside shots where made")

a = float(a)
b = float(b)
c = float(c)

free = a * 1
inside = b * 2
outside = c * 3

total = str(free + inside + outside)

print("total points:" + " " + total)