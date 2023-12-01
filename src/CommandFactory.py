from src.PriorityCommand import PriorityCommand
from src.QueryCommand import QueryCommand
from src.RecordCommand import RecordCommand
from src.ReportCommand import ReportCommand


class CommandFactory:
    def get_command(self, command_type):
        commands = {
            'record': RecordCommand(),
            'query': QueryCommand(),
            'report': ReportCommand(),
            'priority': PriorityCommand(),
        }
        return commands.get(command_type)