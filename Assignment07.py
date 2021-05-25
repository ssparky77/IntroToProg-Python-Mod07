# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Pickling and Error Handling in Python
# ChangeLog (Who,When,What):
# SSparks,5.23.21, began writing code to complete assignment 7
# SSparks,5.24.21, continued completing assignment 7
# SSparks,5.25.21, tested and finalized for submission
# ---------------------------------------------------------------------------- #
import pickle

user_input = ()
strFileName = 'InputData.dat'

# math processing function
def do_math(value_1=0, value_2=0):
    mysum = value_1 + value_2
    diff = value_1 - value_2
    prod = value_1 * value_2
    quot = value_1 / value_2
    return value_1, value_2, mysum, diff, prod, quot


# pickling functions
def save_data_to_file(file_name, list_of_data):
    binfile = open(file_name, 'ab')
    pickle.dump(list_of_data, binfile)
    binfile.close()


def read_data_from_file(file_name):
    binfile = open(file_name, 'rb')
    data = pickle.load(binfile)
    binfile.close()
    return data


# IO functions
def get_numbers(value_1='0', value_2='0'):
    value_1 = int(input("Enter the first number to math: "))
    value_2 = int(input("Enter the second number to math: "))
    return value_1, value_2


def show_calculations(value_1, value_2, mysum, diff, prod, quot):
    print("The Sum of %.f and %.f is: %.f" % (value_1, value_2, mysum))
    print("The Difference of %.f and %.f is: %.f" % (value_1, value_2, diff))
    print("The Product of %.f and %.f is: %.f" % (value_1, value_2, prod))
    print("The Quotient of %.f and %.f is: %.2f" % (value_1, value_2, quot))


# Error Handling & Pickling Code Go Here:

# Error Handling
try:
    user_input = get_numbers()
    math_data = do_math(user_input[0], user_input[1])
    show_calculations(math_data[0], math_data[1], math_data[2], math_data[3], math_data[4], math_data[5])
except Exception as e:
    print("There was an Error!")
    print("Built-in Python error info: ")
    print(e.__str__())

# Pickling Code (Saves the user's input and reports it back)
input_list = [user_input[0], user_input[1]]
save_data_to_file(strFileName, input_list)
print('The user entered: ', read_data_from_file(strFileName))
