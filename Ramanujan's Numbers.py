def generate_taxi_cab_numbers(n):
    generated_number = 0
    v = {}
    c = {}
    i = 0
    while generated_number < n:
        c[i] = i*i*i
        for j in range(i):
            s = c[j] + c[i]
            if s in v:
                generated_number = generated_number + 1
                yield (s, (j, i), v[s])
            v[s] = (j,i)
        i = i + 1


def m(n):
    for x in generate_taxi_cab_numbers(n):
       print(x)

n = int(input("Enter a number\n>"))
print(m(n))