from src.CommandInterface import CommandInterface


class PriorityCommand(CommandInterface):
    def execute(self, args, db, formatter):
        priority_data = db.get_priority_tasks()
        return formatter.format_priority(priority_data)