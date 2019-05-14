# Pick three names and store them in a list.

# Prompt the user to enter their name. If their name is one of the names in the list, display a greeting message that includes their name. If their name isn't in the list, display "Who goes there?"

three_names = ["Alexander", "Goku", "Freeza"]

print("Enter your name")
user_name = input()

if user_name in three_names:
    print("Hello {}!".format(user_name))
else:
    print("Who goes there?")
    
