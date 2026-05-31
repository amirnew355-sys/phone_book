phone_book = {}
print(""" 
 _________________________
|                         |
|__________Menu___________|
|                         |
|   1. Add a Contact      |
|   2. Search a Contact   |
|   3. Delete a Contact   |
|   4. Exit               |
|                         | 
|_________________________|
|_________________________|

""")
while True:
    choice = int(input("num from Menu:"))
    
    if choice == 1:
        name = input("Enter Contact name:")
        phone = input("Enter Contact phone num:")
        phone_book[name]= phone
        print("Contact added!")
    elif choice == 2:
        name1 = input("Contact Name:")
        if name1 in phone_book:
            print(f"Phone:{phone_book[name1]}")
        else:
            print("Contact not found!")
    elif choice == 3:
        name2 = input("Contact name fo delet:")
        if name2 in phone_book:
            del phone_book[name2]
            print("Successfull!")
        else:
            print(f"Contact {name2} not found!")
    elif choice == 4:
        print("Exiting....")
        break
    else:
        print("Invalid!")