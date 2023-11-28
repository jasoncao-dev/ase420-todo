from src.QueryCommand import QueryCommand
from src.RecordCommand import RecordCommand


class CommandFactory:
    def get_command(self, command_type):
        if command_type == 'record':
            return RecordCommand()
        elif command_type == 'query':
            return QueryCommand()
        else:
            return None
