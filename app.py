def main():
    try:
        input_file = input("Enter the name of the file to read: ")
        with open(input_file, 'r') as file:
            content = file.read()
        modified_content = content.lower()
        
        output_file = "modified_" + input_file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content written to {output_file}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don't have permission to read/write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()