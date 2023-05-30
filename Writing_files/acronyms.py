def find_acronym():
    look_up = input("What software acronym would you like to look up?\n")

    found = False
    try:
        with open('software_acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('File not found')
        return

    if not found:
        print('The acronym doesn\'t exist')


def add_acronym():
    acronym = input("What acronym would you like to add?\n")
    definition = input("What is the definition?\n")
    with open('software_acronyms.txt', 'a') as file:
        file.write(f'{acronym} - {definition}\n')


def main():
    choice = input('Do you want to find(F) or add(A) an acronym?\n')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()


main()
