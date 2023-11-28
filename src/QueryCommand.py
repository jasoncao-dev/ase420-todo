from src.CommandInterface import CommandInterface


class QueryCommand(CommandInterface):
    def execute(self, args, db, formatter):
        results = db.query_tasks(args.get('date'), args.get('task'), args.get('tag'))
        if results:
            return formatter.format_query_results(results)
        else:
            return "No tasks found."
