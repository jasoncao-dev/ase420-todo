import re
from datetime import datetime


class InputHandler:
    DATE_PATTERN = r"((?:\d{4}/\d{2}/\d{2})|today)"
    TIME_PATTERN = r"(\d{2}:\d{2}(?:AM|PM)?)"
    TASK_PATTERN = r"'([^']+)'"
    TAG_PATTERN = r":(\S+)"
    RECORD_PATTERN = rf"record {DATE_PATTERN} {TIME_PATTERN} {TIME_PATTERN} {TASK_PATTERN}(?:\s{TAG_PATTERN})?"

    def parse_input(self, command):
        if command.startswith('record'):
            return self._parse_record_command(command)
        elif command.startswith('query'):
            return self._parse_query_command(command)
        elif command.startswith('report'):
            return self._parse_report_command(command)
        elif command.startswith('priority'):
            return self._parse_priority_command()
        else:
            return None, "Invalid command."

    def _parse_record_command(self, command):
        match = re.match(self.RECORD_PATTERN, command)
        if not match:
            return None, "Invalid record format. Use 'record <DATE> <FROM> <TO> '<TASK>' :TAG'."

        date, from_time, to_time, task, tag = match.groups()

        if date.lower() != 'today' and not self._validate_date(date):
            return None, "Invalid date. Ensure date is 'today' or in YYYY/MM/DD format."

        if not self._validate_time(from_time) or not self._validate_time(to_time):
            return None, "Invalid time. Ensure times are in HH:MM or HH:MMAM/PM format."

        date = self._normalize_date(date)
        from_time = self._normalize_time(from_time)
        to_time = self._normalize_time(to_time)
        tag = tag if tag else ''

        return {'command': 'record', 'date': date, 'from_time': from_time, 'to_time': to_time, 'task': task, 'tag': tag}, None

    def _parse_report_command(self, command):
        command_parts = command.split()
        if len(command_parts) != 3:
            return None, "Invalid report command format. Use 'report <FROM DATE> <TO DATE>'."

        from_date, to_date = command_parts[1], command_parts[2]
        if not re.match(self.DATE_PATTERN, from_date) or not re.match(self.DATE_PATTERN, to_date):
            return None, "Invalid date format. Use YYYY/MM/DD."

        return {'command': 'report', 'from_date': from_date, 'to_date': to_date}, None

    def _parse_priority_command(self):
        return {'command': 'priority'}, None

    def _validate_date(self, date_str):
        try:
            datetime.strptime(date_str, '%Y/%m/%d')
            return True
        except ValueError:
            return False

    def _validate_time(self, time_str):
        try:
            if 'AM' in time_str.upper() or 'PM' in time_str.upper():
                datetime.strptime(time_str, '%I:%M%p')
            else:
                datetime.strptime(time_str, '%H:%M')
            return True
        except ValueError:
            return False

    def _normalize_date(self, date_str):
        if date_str.lower() == 'today':
            return datetime.today().strftime('%Y/%m/%d')
        return date_str  # Assuming _validate_date has checked the format already

    def _normalize_time(self, time_str):
        # Assuming _validate_time has checked the format already
        return datetime.strptime(time_str, '%I:%M%p').strftime('%H:%M') if 'M' in time_str.upper() else time_str


    def _parse_query_command(self, command):
        pattern = r"query(?: '([^']*)'|\s(:\S+)|\s(\S+))?"
        match = re.match(pattern, command)
        if not match:
            return None, ("Invalid query format. \n"
                          "Use 'query DATE', 'query TASK', or 'query :TAG'.\n"
                          "Example: query today\n"
                          "Example: query 'Study Python'")

        task, tag, date = match.groups()
        task = task if task else None
        tag = tag[1:] if tag else None  # Remove the colon from tag
        date = self._normalize_date(date) if date else None

        return {'command': 'query', 'task': task, 'tag': tag, 'date': date}, None

    def _convert_to_24_hour_format(self, time_str):
        return datetime.strptime(time_str, '%I:%M%p').strftime('%H:%M') if 'M' in time_str.upper() else time_str

    def _convert_to_12_hour_format(self, time_str):
        time_obj = datetime.strptime(time_str, '%H:%M')
        return time_obj.strftime('%I:%M %p')
