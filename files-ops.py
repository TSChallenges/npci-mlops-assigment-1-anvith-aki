import os
import sys


def create_directory(dir_name):
    os.mkdir(dir_name)
    print("Created Dir: ", dir_name)
    return


def change_directory(dir_name):
    os.chdir(dir_name)
    print("Changed to Dir: ", dir_name)
    return


def delete_directory(dir_name):
    os.rmdir(dir_name)
    print("Deleted Dir: ", dir_name)
    return


def list_dir():
    print("Listing ---")
    print(os.listdir())
    return


def display_pwd():
    print("Current Dir: ", os.getcwd())
    return


def create_file(file_name):

    with open(file_name, 'w') as f:
        pass
    print(f"File '{file_name}' is created")

    return


def write_file(file_name):

    contents = input("Enter the contents into the file")
    with open(file_name, 'a') as f:
        f.write(contents + '\n')
    print(f"Contents written to file successfully")

    return


def read_file(file_name):

    with open(file_name, 'r') as f:
        print(f.read())

    return


def delete_file(file_name):

    os.remove(file_name)
    return


def main():
    while True:
        print("1. Create a file")
        print("2. Write to a file")
        print("3. Read a file")
        print("4. Delete a file")
        print("5. Create a dir")
        print("6. Delete a dir")
        print("7. Change to dir")
        print("8. list dir")
        print("9. Current Work Dir")
        print("0. Exit")
        choice = input("Enter your choice here: ")

        if choice == '1':
            file_name = input("1. Enter the file name: ")
            create_file(file_name)
        elif choice == '2':
            file_name = input("2. Enter the file name: ")
            write_file(file_name)
        elif choice == '3':
            file_name = input("3. Enter the file name: ")
            read_file(file_name)
        elif choice == '4':
            file_name = input("4. Enter the file name: ")
            delete_file(file_name)
        elif choice == '5':
            dir_name = input("5. Enter the dir name: ")
            create_directory(dir_name)
        elif choice == '6':
            dir_name = input("6. Enter the dir name: ")
            delete_directory(dir_name)
        elif choice == '7':
            dir_name = input("7. Enter the dir name: ")
            change_directory(dir_name)
        elif choice == '8':
            list_dir()
        elif choice == '9':
            display_pwd()
        elif choice == '0':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
