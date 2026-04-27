nums = list(range(10))

# every second number
print(nums[::2])


# reversed(using slicing)
print(nums[::-1])

# loop with range(3 & 8)
for i in range(3,8):
    print(i)

# enumerate on list of fruits.
fruits=["apple", "banana", "orange"]
for index,fruits in enumerate (fruits):
    print( index, ":",  fruits)



# chatgpt helped me this.
my_dictionary= {
    "A":1,
    "B":2
}


for k,v in my_dictionary.items():
    print(k, ":", v)