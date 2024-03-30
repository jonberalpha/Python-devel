from mymodule import DataProcessor, additional_function, string_example, list_example
import sys

def main():
  # Check if the correct number of command-line arguments is provided
  if len(sys.argv) != 2:
    print("Usage: python main.py <input_file>")
    sys.exit(1)

  input_file = sys.argv[1]

  # Create an instance of the DataProcessor class
  data_processor = DataProcessor(input_file)

  # Process data and print the result
  result = data_processor.process_data()
  data_processor.print_result(result)
  
  additional_function()
  string_example()
  list_example()

if __name__ == "__main__":
  main()

