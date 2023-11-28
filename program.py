from TodoCLI import TodoCLI


def main():
    cli_app = TodoCLI()
    print("Welcome to the CLI To-Do List App! Type 'help' for usage instructions.")
    cli_app.display_help()

    while True:
        user_input = input("> ")

        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'help':
            cli_app.display_help()
        else:
            response = cli_app.execute_command(user_input)
            print(response)


if __name__ == '__main__':
    main()
