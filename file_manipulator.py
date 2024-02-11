import sys

def reverse_file(input_path, output_path):
    with open(input_path, 'r') as file:
        content = file.read()
    with open(output_path, 'w') as file:
        file.write(content[::-1]) # Write reverse content

def copy_file(input_path, output_path):
    with open(input_path, 'rb') as file:
        content = file.read()
    with open(output_path, 'wb') as file:
        file.write(content) # Write the same content

def duplicate_contents(input_path, n):
    with open(input_path, 'r') as file:
        content = file.read()
    new_content = content * int(n) # Get n contents
    with open(input_path, 'w') as file:
        file.write(new_content)

def replace_string(input_path, needle, new_string):
    with open(input_path, 'r') as file:
        content = file.read()
    new_content = content.replace(needle, new_string) # Get needle from haystack
    with open(input_path, 'w') as file:
        file.write(new_content)

def main():
    if len(sys.argv) < 2: # Require command and arguments
        print("Usage: python file_manipulator.py [command] [arguments]")
        sys.exit(1)
        
    command = sys.argv[1]
    args = sys.argv[2:]
    
    if command == 'reverse' and len(args) == 2:
        reverse_file(args[0], args[1])
    elif command == 'copy' and len(args) == 2:
        copy_file(args[0], args[1])
    elif command == 'duplicate-contents' and len(args) == 2:
        duplicate_contents(args[0], args[1])
    elif command == 'replace-string' and len(args) == 3:
        replace_string(args[0], args[1], args[2])
    else:
        print("Invalid command or number of arguments")
        print("Usage: python file_manipulator.py [command] [arguments]")

if __name__ == "__main__":
    main()
