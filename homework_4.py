from collections import defaultdict

# Декоратор input_error
def input_error(func):
    """Декоратор для обробки поширених помилок введення."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
        except KeyError:
            return "Contact not found."
    return inner

def parse_input(user_input: str):
    """Парсить введення користувача на команду та аргументи."""
    try:
        cmd, *args = user_input.strip().lower().split()
    except ValueError:
        return "", []
    return cmd, args


@input_error
def add_contact(args, contacts):
    """Додає новий контакт до словника контактів."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """Змінює номер телефону для існуючого контакту."""
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    """Показує номер телефону для конкретного контакту."""
    name = args[0]
    return contacts[name]

def show_all(contacts):
    """Показує всі контакти у словнику."""
    if not contacts:
        return "No contacts saved."
    
    result = "All contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result

def main():
    """Основна функція для бота-помічника."""

    # Створюємо словник для зберігання контактів всередині main()
    contacts = {} 

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()