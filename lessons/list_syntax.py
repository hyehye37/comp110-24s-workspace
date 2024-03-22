"""Demosntrate Basic List Syntax"""

#initalize an empty list
grocery_list: list[str] = list() # <- list constructor
grocery_list: list[str] = [] # <- literal
#lines 4 and 5 are doing the same thing and can have one or the other 

print(grocery_list)

#add itmes to a list (one at a time; convenient when you already have a list and just trying to add something) 
grocery_list.append("bananas")
grocery_list.append("Milk")
grocery_list.append("bread")

print("After appending:")
print(grocery_list)

#Create an already populated list; the previous two steps compiled in one; still can use append  
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("populated list:")
print(grocery_list2)
grocery_list2.append("eggs")
print(grocery_list2)

#indexing
print("Print first element of string")
print(grocery_list[0])

#modifying by index
print("Before change: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print("After change:")
print(grocery_list)


#You can have duplicates
grocery_list.append("almond milk")
print("Add almond milk again:")
print(grocery_list)

#Measuring length
print("Length of list:")
print(len(grocery_list))

#Removing an item
grocery_list.pop(1)
print("After removing almond milk:")
print(grocery_list)


#function name: display
#parameter: list[str]
#return nothing
#Print out the list

def display(word: list[str]) -> None:
    print(word)
display(grocery_list)
x = display(["Alyssa", "Erin", "AK"])
print(x) #will print out nothing since the function "display" retunrs nothing 

# Create a list
# Name: create
# Parameters: str and str 
# Return value: list[str] 
# Put both parameters into a list and return that list 
def create(word1: list[str], word2: list[str]) -> list[str]:
    my_list: list[str] = [word1, word2]
    return my_list
print(create("Hello", "World"))