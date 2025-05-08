def generate_odd_numbers(a):
    result = []
    count = 0
    num = 1

    while count < a:
        result.append(str(num))
        num += 2
        count += 1
    return ",".join(result)

a = int(input())
series = generate_odd_numbers(a)

print("Generated odd numbers :" , series)
