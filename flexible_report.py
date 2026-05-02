def total(*numbers):
    return sum(numbers)
print(total(1,2,3))
print(total(4,5,6))
print(total())


def profile(**info):
    for key, value in info.items():
        print(key + ":", value)
profile(name = "shakir ", age= 21, country= "ethiopia")


profile(name="abdullahi ", age = 24, country="somalia")


