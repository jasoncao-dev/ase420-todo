from src.CommandInterface import CommandInterface


class ReportCommand(CommandInterface):
    def execute(self, args, db, formatter):
        from_date, to_date = args['from_date'], args['to_date']
        report_data = db.generate_report(from_date, to_date)
        return formatter.format_report(report_data)