# User Manual for the Command Line Interface (CLI) Time Management App:

## Introduction: 
Welcome to the CLI To-Do App, a simple and intuitive tool designed to help you manage your time and tasks straight from the command line. This tool allows you to record your activities with ease and query them to stay organized.

## Installation: 

To install the CLI To-Do App, please follow these steps:

1. Ensure that Python 3.x and required packages are installed on your system.
2. Download the application files to a local directory on your computer.
3. Navigate to the application directory in your command-line interface.

## Usage:

### Recording a Task: 
To record a new task, use the following format:

```bash
record <DATE> <FROM TIME> <TO TIME> '<TASK DESCRIPTION>' :TAG
```
- `<DATE>`: The date when the task is performed. It can be specified as today or in the format YYYY/MM/DD.
- `<FROM TIME>` and `<TO TIME>`: The start and end times of the task, given either in 24-hour format (HH:MM) or with AM/PM designation (HH:MMAM/PM).
- `<TASK DESCRIPTION>`: A brief description of the task, enclosed in single quotes.
- `<:TAG>`: An optional tag to categorize the task. It must be prefixed with a colon.

Example:
```bash
record today 09:30 10:30 'Studied Python' :STUDY
```

### Querying Tasks: 
To query the database for your recorded tasks, you can use the following format:

```bash
query <DATE|'TASK'|:TAG>
```
- `<DATE>`: Get all tasks recorded on a specific date.
- `<'TASK'>`: Retrieve all activities related to a specific task description (enclosed in single quotes).
- `<:TAG>`: Fetch all activities tagged with a specific category.

Examples:
```bash
query today             # Get all tasks for today
query 'Studied Python'  # Get all tasks with 'Studied Python' in the description
query :STUDY            # Get all tasks tagged with STUDY
```

### Generating a Time Usage Report:
To generate a report of your time usage for a specific date range, use the following format:

```bash
report <FROM DATE> <TO DATE>
```
- `<FROM DATE>`: The start date of the report range in the format YYYY/MM/DD.
- `<TO DATE>`: The end date of the report range in the format YYYY/MM/DD.

Example:
```bash
report 2021/01/01 2022/01/01 # Generates a report from start to end date
```

### Identifying Time Priorities:
To see a sorted list of tasks based on time spent, use the following command:

```bash
priority
```
- This command does not require additional arguments and will list tasks prioritized by total time spent on them.


Example:
```bash
priority # Lists tasks by priority of time spent
```

### Exiting the Application: 
To exit the CLI To-Do App, simply type:
```bash
exit
```
### Help: 
If you need assistance with the command formats or usage, type `help` to display the help message, which will provide the information covered in this manual.