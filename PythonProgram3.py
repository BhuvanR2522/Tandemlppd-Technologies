a = int(input())

if a % 2 == 0:
    x = a // 2
else:
    x = (a + 1) // 2

odd_number = []
for i in range(x):
    odd_number.append(str(2 * i + 1))

print("Series of odd number :" ,",".join(odd_number))