#Declare an empty list
bleh = []
meh = list()
#declare a non empty list
yummy = ["Pizza" , "Lasagne", "Fish and Chips"]
#print an entire list
print(yummy)
#printing a single item
print(yummy[2])
#printing some items
print(yummy[:2])
#add elements to our list (expand it) - adding at the end
print(bleh)
bleh.append("Sea food")
bleh.append("Soup")
bleh.append("Liver")
print(bleh)

#adding multiple items to the list, based on user input
for i in range(5):
    yummy.append(input("Enter new yummy food: ")) #expand list
    #yummy[i] = input() - replace items
print(yummy)
#adding new items at specific positions on the list
print(bleh)
bleh.insert(1, "Mashed potatoes")
print(bleh)
bleh.insert(3, "Cabbage")
print(bleh)
#remove an item from list, based on name
if "Potatoes" in bleh:
  bleh.remove("Potatoes")
bleh.remove("Soup")

#remove item by index
x =bleh.pop(1)
print(bleh)
print(x)
#alternative way of deleting an item via index
del bleh[1]
print(bleh)
#extending a list
bleh.extend(["Fish", "Frankfurters", "Beetroot"])
print(bleh)
bleh.extend(yummy)
print(bleh)
#checking for particular data type
lista =["Fred", True, 6, 8, -3.6, False, "Lala", 55]
for item in lista:
    if isinstance(item, int):
        print(item)