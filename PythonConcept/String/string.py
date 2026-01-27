# String

name1 = "raje"                           # defining the string by different ways
name2 = 'maharaje'
name3 = str("shashan")

print(name1, name2, name3 )

# string concatenation

print(name1 + " gadpati")
print(name1 * 3)                  # op: rajerajeraje

# string immutable

std_1 = "ram"
std_2 = "ram"

print(id(std_1))        # op: 2625168489328
print(id(std_2))        # op: 2625168489328      same ids for 2 different variable | because of same string value
