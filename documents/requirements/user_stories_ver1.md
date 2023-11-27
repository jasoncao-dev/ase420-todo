# Requirements (ver 1) - Time Management Application

## User Stories

As a student, I want a personal time-management application so that I can record and query my time usage to better manage my daily activities.

## Breakdown of Requirements:

### Recording Time Usage
- As a user, I want to input the date, start time, end time, task description, and tags in the format “DATE FROM TO TASK TAG” so that I can record my time usage in a database.
- As a user, I expect the application to support different date formats such as “today” and “YYYY/MM/DD” for ease of use.
- As a user, I want to specify "AM" or "PM" with the 'FROM' and 'TO' times to accurately record my time slots.

### Querying Time Usage
- As a user, I want to query the database using date, task description, or tag so that I can retrieve specific records of my activities.
- As a user, I expect the query to return all activities for a given date when I input “query DATE”.
- As a user, I want the query to return all activities related to a specific task when I input “query 'TASK' ”.
- As a user, I would like the query to return all activities associated with a particular tag when I input “query :TAG”.

### Data Persistence
- As a user, I need the time usage data to be stored persistently in a SQLite database so that my records are maintained across application uses.

### Input Validation and Feedback
- As a user, I want the application to validate the input format and provide feedback if the input is incorrect so that I can ensure the data is recorded accurately.
- As a user, I expect to receive confirmation upon successfully recording a task or querying the database.

### Ease of Use
- As a user, I want clear instructions on how to use the command-line application so that I can efficiently interact with it without confusion.

### Error Handling
- As a user, I expect the application to handle errors gracefully and to provide helpful error messages if something goes wrong.

### Help and Documentation
- As a user, I want to have access to a help command or documentation so that I can refer to the usage instructions and examples whenever necessary.

### Additional Requirements:
- The application should include an intuitive command-line parser to handle different commands (record, query, help).
- The application must include functionality for adding, retrieving, and displaying records from an SQLite database.
- The application's code should follow clean code principles and design patterns where applicable, to ensure maintainability and scalability.