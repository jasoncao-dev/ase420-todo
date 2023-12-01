class Formatter:
    def format_query_results(self, results):
        formatted_results = [f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}" + (f" {row[5]}" if row[5] is not None else "") for row in
                 results]
        return "\n".join(formatted_results)

    def format_report(self, report_data):
        lines = [f"{row[1]} {row[2]} {row[3]} {row[4]}" + (f" {row[5]}" if row[5] is not None else "") for row in
                 report_data]
        return "\n".join(lines)

    def format_priority(self, priority_data):
        lines = []
        for task, total_time in priority_data:
            formatted_time = self.format_duration(total_time)
            lines.append(f"Task: {task}, Time Spent: {formatted_time}")
        return "\n".join(lines)

    def format_duration(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
