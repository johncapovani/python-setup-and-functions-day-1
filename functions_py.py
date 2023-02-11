import time


# Prompt: A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.

def hello():
        print("Hi user, welcome to this spicy python application")

hello()

# Prompt: A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.

def pack(arg1, arg2, arg3):
        
    return [arg1, arg2, arg3]

# Prompt: A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.

# Took a different approach using enumerate

start_time = time.time()
def eat_lunch(lunchbox_items):
      for index, item_value in enumerate(lunchbox_items, start=0):
        if index == 0:
            print(f"First I eat a {item_value}")
        elif index > 0:
            print(f"Next I eat a {item_value}")
        else:
             print("My lunchbox is empty! :(")


lunchbox_items = ["hot dog", "chip", "pickle", "cookie"]

eat_lunch(lunchbox_items)

print("My program took", time.time() - start_time, "seconds to run")

start_time = time.time()
def eat_lunch_solution(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")
            

eat_lunch_solution(["apple", "banana", "sandwich", "cookie"])
print("Solution program took", time.time() - start_time, "seconds to run")
# Solution code for this prompt was certainly faster... Leave it to the professionals lol

