age = int(input("How Old Are You?\n"))
decades = age // 10

# Modulo can show the reminder of a value, and we store this remainder as a seperate variable "years"
years = age % 10

print("You are " + str(decades) + 
      " decades and " + str(years) + " years old.")