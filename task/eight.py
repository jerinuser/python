# # one=int(input('enter the number:'))
# # two=int(input('enter the number:'))
# # print(one+two)


# # def print_multiplication_table(number):
# #     print(f"Multiplication Table for {number}:")

# #     for i in range(1, 11):
# #         result = number * i
# #         print(f"{number} x {i} = {result}")

# # # Example usage
# # number = int(input('neter the number :'))
# # print_multiplication_table(number)

# # hi='hello world'

# # reverse=hi[::-1]

# # print(reverse)

# def read_and_print_file(file_path):
#     """
#     Read the contents of a text file and print them.

#     Parameters:
#     file_path (str): The path to the text file.
#     """
#     try:
#         # Open the file in read mode
#         with open(file_path, 'r') as file:
#             # Read the contents of the file
#             contents = file.read()
#             # Print the contents
#             print(contents)
#     except FileNotFoundError:
#         print(f"The file at {file_path} was not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# file_path = 'example.txt'
# read_and_print_file(file_path)

name = ("jerin",1)
print(type(name))