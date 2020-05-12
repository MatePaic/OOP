# initialize
a = []

# create the table (name, age, job)
a.append(["Nick", 30, "Doctor"])
a.append(["John",  8, "Student"])
a.append(["Paul", 22, "Car Dealer"])
a.append(["Mark", 66, "Retired"])

# sort the table by age
import operator
a.sort(key=operator.itemgetter(1))

a.sort(key=lambda elem: elem[1])


# print the table
print(a)
