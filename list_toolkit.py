cities = ["mogadishu ", "hargeisa ", "jijiga ", "nairobi ", "degehbur "]
print("first city:", cities[0])
print("last city:", cities[-1])
# adding one more city in our code 
cities.append("berbera ")
print(cities)

#removing a city using .pop()
removed_city = cities.pop(1)
print("removed_city:", removed_city)

# length of the list
print(len(cities))
