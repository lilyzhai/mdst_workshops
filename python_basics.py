"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import base64


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    val = num
    if val % 2 == 0 :
        print("even!")
    else :
        print("odd!")



def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    import random
    ranNum = random.randint(1,9)
    guessNum = (input("Guess: "))
    while guessNum != "exit" :
        if (int(guessNum) > ranNum) :
            print("Too high")
        elif (int(guessNum) < ranNum) :
            print("Too low")
        elif (int(guessNum) == ranNum) :
            print("You got it!")
            break;
        guessNum = (input("Guess: "))




def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    test = string
    newTest = test[::-1]
    if test == newTest:
        print("True")
    else :
        print("False")


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """

    name = base64.b64encode(username.encode()).decode('utf-8')
    data = base64.b64encode(password.encode()).decode('utf-8')

    with open(filename, "w") as my_file:
        my_file.write(name + "\n")
        my_file.write(data + "\n")


def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """

    with open(filename, "r+") as my_file:
        name = my_file.readline()
        data = my_file.readline()
        de_name = base64.decodestring(name.encode('utf-8'))
        de_data = base64.decodestring(data.encode('utf-8'))
        print("username: ", de_name)
        print("password: ", de_data)
        if password != None :
            new_pass = base64.b64encode(password.encode()).decode('utf-8')
            my_file.write(data + "\n")




if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
