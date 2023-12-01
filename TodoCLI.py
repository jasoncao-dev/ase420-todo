from src.InputHandler import InputHandler
from src.Database import Database
from src.CommandFactory import CommandFactory
from src.Formatter import Formatter


class TodoCLI:

    def __init__(self):
        self.db = Database('todo.db')
        self.input_handler = InputHandler()
        self.command_factory = CommandFactory()
        self.formatter = Formatter()

    def execute_command(self, command_str):
        if command_str == 'help':
            return self.display_help()

        args, error = self.input_handler.parse_input(command_str)

        if error:
            return error

        command = self.command_factory.get_command(args['command'])

        if command:
            return command.execute(args, self.db, self.formatter)
        return "Invalid command."

    def display_help(self):
        print("Usage Instructions:")
        print("\tTo record a task:")
        print("\t\trecord <DATE> <FROM TIME> <TO TIME> '<TASK DESCRIPTION>' :TAG")
        print("\t\tExamples:")
        print("\t\t\trecord today 09:30 10:30 'Study Python' :STUDY")
        print("\t\t\trecord 2023/04/01 07:00PM 09:00PM 'Read a book'")
        print()
        print("\tTo query tasks:")
        print("\t\tquery <DATE> or 'TASK DESCRIPTION' or :TAG")
        print("\t\tExamples:")
        print("\t\t\tquery today")
        print("\t\t\tquery 'Study Python'")
        print("\t\t\tquery :STUDY")
        print()
        print("\tTo generate a time usage report:")
        print("\t\treport <FROM DATE> <TO DATE>")
        print("\t\tExamples:")
        print("\t\t\treport 2021/01/01 2022/01/01")
        print()
        print("\tTo see tasks sorted by time spent on them:")
        print("\t\tpriority")
        print("\t\tExample:")
        print("\t\t\tpriority")
        print()
        print("\tType 'exit' to close the application.")