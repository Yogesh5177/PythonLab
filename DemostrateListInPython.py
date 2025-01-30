# Creating a list
fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]

# Printing the entire list
print("Fruit List:", fruits)

# Accessing elements using indexing
print("First fruit:", fruits[0])  # Apple
print("Last fruit:", fruits[-1])  # Orange

# Modifying an element
fruits[1] = "Blueberry"
print("Updated List:", fruits)

# Adding elements to the list
fruits.append("Grapes")  # Adding an element at the end
print("After Adding Grapes:", fruits)

# Removing an element
fruits.remove("Cherry")
print("After Removing Cherry:", fruits)

# Looping through the list
print("List of Fruits:")
for fruit in fruits:
    print(fruit)

# Finding the length of the list
print("Total number of fruits:", len(fruits))
