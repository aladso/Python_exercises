# Guess if the string introduced by a user is a palindrome or not

x = 1

while x == 1:

    text = str(input("Please insert something: "))
    print("You inserted " + text)

    new_text = text[::-1]  # This way we read the string backwards. Ex. text[6:-1] --> from 6 to 0, not from 0 to 6
    # This line starts reading from the last number to the first one: [: (highest num):-1 (position 0)]
    print(new_text)

    if new_text == text:
        print("The text you typed is a palindrome")
    else:
        print("The text you typed is not a palindrome")

    user = str(input("Do you want to repeat? [y/n]: "))
    if user == "n":
        x = 0
