# Functions with input

#def greet_with_name(name):
 #   print(f"Hello {name}")
  #  print(f"How do you do {name}?")


#greet_with_name("Jack Bauer")


#def greet(name, greeting):
 #   print(f"{greeting} {name}")

#greet("Sneha", "Hii!")

#def greet_with(name , location ) :
 #   print(f"Hello!! {name} ")
  #  print(f"What is it like in {location}")
#greet_with(location= "london" , name = "Sneha")


def calculate_love_score(name1, name2):
    # Combine the names
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    # Count letters in "true"
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e1 = lower_names.count("e")
    first_digit = t + r + u + e1

    # Count letters in "love"
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e2 = lower_names.count("e")
    second_digit = l + o + v + e2

    # Calculate score
    score = int(str(first_digit) + str(second_digit))
    print(score)

# Call the function outside
calculate_love_score("Sneha Prajapati", "Payal Kawale")

