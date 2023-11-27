from src.InputHandler import InputHandler
from src.Database import Database


class TodoCLI:

    def __init__(self):
        self.db = Database('todo.db')
        self.input_handler = InputHandler()

    def execute_command(self, command):
        args, error = self.input_handler.parse_input(command.strip())

        if error:
            return error + "\nType 'help' for usage instructions."

        if args['command'] == 'record':
            self.db.add_task(args['date'], args['from_time'], args['to_time'], args['task'], args['tag'])
            return "Task recorded successfully."
        elif args['command'] == 'query':
            results = self.db.query_tasks(args.get('date'), args.get('task'), args.get('tag'))
            if results:
                formatted_results = []
                for result in results:
                    formatted_result = list(result)
                    formatted_result[1] = self.input_handler._convert_to_12_hour_format(result[1])
                    formatted_result[2] = self.input_handler._convert_to_12_hour_format(result[2])
                    formatted_results.append(" ".join(map(str, formatted_result)))
                return "\n".join([f"{task}" for task in formatted_results])
            else:
                return "No tasks found."
        else:
            return "Invalid command."

    def display_help(self):
        print("Usage Instructions:")
        print("\tTo record a task:")
        print("\t\trecord <DATE> <FROM TIME> <TO TIME> '<TASK>' :TAG")
        print("\t\tExamples:")
        print("\t\t\trecord today 09:30 10:30 'Study Python' :STUDY")
        print("\t\t\trecord 2023/04/01 07:00PM 09:00PM 'Read a book'")
        print()
        print("\tTo query tasks:")
        print("\t\tquery <DATE> or 'TASK' or :TAG")
        print("\t\tExamples:")
        print("\t\t\tquery today")
        print("\t\t\tquery 'Study Python'")
        print("\t\t\tquery :STUDY")
        print()
        print("\tType 'exit' to close the application.")


def main():
    cli_app = TodoCLI()
    print("Welcome to the CLI To-do List App!")
    cli_app.display_help()
    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            print("Thank you for using the app. Goodbye!")
            break
        elif user_input.lower() == 'help':
            cli_app.display_help()
        else:
            response = cli_app.execute_command(user_input)
            print(response)


if __name__ == '__main__':
    main()
