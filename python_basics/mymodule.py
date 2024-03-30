class DataProcessor:
  def __init__(self, input_file):
    self.input_file = input_file
    self.data = self.process_input()

  def process_input(self):
    # Read data from the input file
    with open(self.input_file, 'r') as file:
      data = [int(line.strip()) for line in file]

    return data

  def process_data(self):
    # Example: Sum all the numbers in the list
    return sum(self.data)

  def print_result(self, result):
    # Print the result
    print(f"Result: {result}")

# Other functions can be added to the module as well

# Example function
def additional_function():
  print("This is an additional function.")

def string_example():
  # Creating strings
  string1 = 'Hello, World!'
  string2 = "Python is great."

  # Accessing characters in a string
  print(string1[0])   # Output: H
  print(string1[7])   # Output: W

  # Slicing a string
  substring = string1[7:12]  # Output: World

  # Concatenating strings
  new_string = string1 + ' ' + string2  # Output: Hello, World! Python is great.

def list_example():
  # Creating a list
  my_list = [1, 2, 3, 'apple', 'banana']

  # Accessing elements in a list
  print(my_list[0])       # Output: 1
  print(my_list[3])       # Output: apple

  # Modifying elements in a list
  my_list[1] = 'orange'

  # Adding elements to a list
  my_list.append('grape')

  # Removing elements from a list
  my_list.remove(3)
  del my_list[4]

  # Iterating through a list
  print()
  for item in my_list:
    print(item)

  # List comprehension
  squared_numbers = [x**2 for x in range(5)]  # Output: [0, 1, 4, 9, 16]
  print()
  for squared_number in squared_numbers:
    print(squared_number)


