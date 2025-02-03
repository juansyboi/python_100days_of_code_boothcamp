days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

print(days) #print all values in list
print(days[1]) #print tuesday value in list
print(days[-1]) #print the last value in list 


#additional function
names = ["John"]

names.append("Michael") #add new value starting at the last
print(names)
names.extend(["Jandayan", "Otom"]) #add new values in the list from the iterable
print(names)
names.insert(0, "Mr. ") #insert value in any position in the list
print(names)
names.sort(key=str, reverse=False) #sort in ascending but not reverse
print(names)
names.reverse()
print(names)
names.remove("Mr. ")
print(names)
names.clear()
print(names)
