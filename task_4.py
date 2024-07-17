def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Command requires more arguments."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def show_all(args, contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    commands = {
        "add": add_contact,
        "phone": get_phone,
        "all": show_all,
    }
    
    while True:
        user_input = input("Enter a command: ").strip().split()
        if not user_input:
            print("Please enter a command.")
            continue
        
        command = user_input[0]
        args = user_input[1:]
        
        if command in commands:
            print(commands[command](args, contacts))
        else:
            print("Unknown command. Available commands: add, phone, all")

if __name__ == "__main__":
    main()
