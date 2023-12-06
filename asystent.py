def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact does not exist."
        except ValueError:
            return "Invalid input."
        except IndexError:
            return "Invalid input."
        except TypeError:
            return "Contact does not exist."
    return inner

contacts = {}

def hello():
    return "How can I help you?"
@input_error
def add(name, number):
    contacts[name] = number
    return f"Added {name} number: {number}."
@input_error
def change(name, number):
    contacts[name] = number
    return f"{name} number has been changed to: {number}"
@input_error
def phone(name):
    return f"{name} phone: {contacts[name]}"
    
def show(contacts):
    if not contacts:
        return "Contacts list is empty."
    contacts_list = []
    for name, number in contacts.items():
        contacts_list.append(f"{name}: {number}")
    return "\n".join(contacts_list)

def main():

    menu = "Commands:\n<hello>\n<add>\n<change>\n<phone>\n<show>\n<exit>"
    print(menu)
    while True:
        
        command = input("Enter command: ").lower()
        
        
        if command == "hello":
            print(hello())

        elif command.startswith("add"):
            x = command.split(maxsplit=2)
            if len(x) == 3:
                i, name, number = x
                print(add(name, number))
            else:
                print("Enter 'add name phone_number'")


        elif command.startswith("change"):
            x = command.split(maxsplit=2)
            if len(x) == 3:
                i, name, number = x
                print(change(name, number))
            else:
                print("Enter 'change name new_number'")

        elif command.startswith("phone"):
            x = command.split(maxsplit=1)
            if len(x) == 2:
                i, name = x
                print(phone(name))
            else:
                print("Enter 'phone name'")

        elif command == "show":
            print(show(contacts))
            
        elif command in ["exit", "close", "goodbye"]:
            print("Good Bye!")
            break
        
        elif command == ".":
            break
        else:
            print("Unknown command.")
            print(menu)

if __name__ == "__main__":
    main()

