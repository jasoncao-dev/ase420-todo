from src.CommandInterface import CommandInterface


class RecordCommand(CommandInterface):

    def execute(self, args, db, formatter):
        db.add_task(args['date'], args['from_time'], args['to_time'], args['task'], args['tag'])
        return "Task recorded successfully."
