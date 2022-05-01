import sys  # 2

# 1 - Write a Python program to print the following string in a specific format.
print("Twinkle, twinkle, little star,"
      "\n\tHow I wonder what you are! "
      "\n\t\tUp above the world so high, "
      "\n\t\tLike a diamond in the sky. "
      "\nTwinkle, twinkle, little star, "
      "\n\tHow I wonder what you are")

# 2 - Write a Python program to get the Python version you are using.
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

# # 3 - Write a Python program to display the current date and time.
# import datetime
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# # 4 - Accepts the radius of a circle from the user and compute the area.


# 5 - Accepts the user's first and last name and print them in reverse order with a space between them.
sample6_fname = input("Enter first name: ")
sample6_lname = input("Enter last name: ")
print("Hello", sample6_lname, ",", sample6_fname)
