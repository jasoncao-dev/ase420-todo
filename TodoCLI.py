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