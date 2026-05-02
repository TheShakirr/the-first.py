course_name = "Python Bootcamp"  # global variable


def courseName():
    course_name = "Advanced Python Bootcamp"  # local
    print(course_name)


print(course_name)
courseName()
print(course_name)


# global variables exists outside the func,
# local variables exists only inside the func............
