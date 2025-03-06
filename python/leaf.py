import csv
import time

def leaf_details_to_csv(file_pat, detail):
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Ninja_Id', 'Name', 'Age', 'Level'])
        writer.writeheader()
        writer.writerows(details)




def add_ninja(detail):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
    except FileNotFoundError:
        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Ninja_Id', 'Name', 'Age', 'Level'])
            writer.writeheader()
            writer.writerows(details)

    while True:
        ninja_id = round(time.time() * 1000)
        name = input("Enter name: ")
        age = input("Enter age: ")
        level = input("Enter level: ")
        detail.append({'Ninja_Id': ninja_id, 'Name': name, 'Age': age, 'Level': level})
        print("Your ninja id is :", ninja_id)
        print("If you want to continue adding enter 'yes' otherwise press any key to go back for menu")
        temper = input("yes or no: ")
        temp = temper.lower()
        if temp != 'yes':
            break
    return detail


def delete_ninja(detail):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

        ninja_id = int(input("Enter ninja id to delete: "))
        for d in details:
            if d['Ninja_Id'] == ninja_id:
                details.remove(d)
                break
            else:
                print("No details present")
    except FileNotFoundError:
        pass


def modify_ninja_details(detail):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

        ninja_id = int(input("Enter ninja id to modify: "))
        for d in details:
            if d['Ninja_Id'] == ninja_id:
                print("What do you want to modify?")
                print("1. Name")
                print("2. Age")
                print("3. Level")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    d['Name'] = input("Enter new name: ")
                elif choice == 2:
                    d['Age'] = input("Enter new age: ")
                elif choice == 3:
                    d['Level'] = input("Enter new level: ")
                break
            else:
                print("No details present")
    except FileNotFoundError:
        pass


def print_details(detail):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

        print("Ninja id\tName\tAge\tLevel")
        for d in details:
            print("{}\t{}\t{}\t{}".format(d['Ninja_Id'], d['Name'], d['Age'], d['Level']))
    except FileNotFoundError:
        pass


def display_menu(detail):
    while True:
        print("\nMenu:")
        print("1. Add ninja details")
        print("2. Delete ninja details")
        print("3. Modify ninja details")
        print("4. Print details")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_ninja(details)
        elif choice == '2':
            delete_ninja(details)
        elif choice == '3':
            modify_ninja_details(details)
        elif choice == '4':
            print_details(details)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")


file_path = 'leaf_details.csv'
details = []


try:
    with open(file_path, 'r') as file:
        reade = csv.DictReader(file)
        details = [row for row in reader]
except FileNotFoundError:
    pass

display_menu(details)
leaf_details_to_csv(file_path, details)

