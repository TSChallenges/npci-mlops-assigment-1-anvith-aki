import re


def grep(pattern, file_name):
    with open(file_name, 'r') as fp:
        for line in fp:
            if re.search(pattern, line):
                print(line.strip())
    return


def sed(old_pattern, new_pattern, file_name):
    with open(file_name, 'r') as fp:
        lines = fp.readlines()
    with open(file_name, 'w') as fp:
        for line in lines:
            updated_line = re.sub(old_pattern, new_pattern, line)
            fp.write(updated_line)

    print("Pattern replaced successfully.")
    return


def awk(n, file_name):
    with open(file_name, 'r') as fp:
        for line in fp:
            columns = line.strip().split()
            if n <= len(columns):
                print(columns[n - 1])  # To Convert 1-based index to 0-based
    return


def main():
    file_name = input("Enter the file name: ")
    command = input("Enter the command - grep, sed, awk: ")

    if command == 'grep':
        pattern = input("Enter the pattern: ")
        grep(pattern, file_name)
    elif command == 'sed':
        old_pattern = input("Enter old pattern: ")
        new_pattern = input("Enter new pattern: ")
        sed(old_pattern, new_pattern, file_name)
    elif command == 'awk':
        n = input("Enter the column number: ")
        num = int(n)
        awk(num, file_name)
    else:
        print("Command is invalid")


if __name__ == "__main__":
    main()
