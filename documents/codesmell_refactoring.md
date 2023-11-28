# Code Smells and Refactorings

## Code Smells:
Below are some code smells that I have identified in the codebase on Nov 24, 2023. Here is the [source code](https://github.com/jasoncao-dev/ase420-todo/commit/efc12d53cab18e943f5711a796a2223e095553e1) for reference.
1. **Large Class**: `TodoCLI` in `program.py` is handling multiple responsibilities like interacting with the command line, invoking database operations, and formatting the results.
2. **Feature Envy**: The methods in `TodoCLI` seem to be more interested in the data of other classes (`InputHandler` and `Database`), indicating they may be better placed within those classes.
3. **Inappropriate Intimacy**: `TodoCLI` seems to be closely tied to implementation details of `Database` and `InputHandler`, such as accessing inherited or private methods.
4. **Long Method**: The method `execute_command` in `TodoCLI` is doing too many things, such as parsing commands, interacting with the database, and formatting output.
5. **Duplicated Code**: Similar formatting logic is repeated in `execute_command` for query results.
6. **Data Class**: Database is a data class that only contains data access with no additional logic.
7. **Improper Use of Object-Oriented Design**: Potential lack of encapsulation where direct manipulation of class internals occurs.

## Refactoring Strategy using SOLID Principles and OOP:
1. **Single Responsibility Principle**: Refactor `TodoCLI` so that it only manages user interactions. Extract data formatting and database interactions to separate classes.
2. **Open/Closed Principle**: Design new classes to allow for easy extension without modification. For example, introduce an interface for formatting that can have different implementations.
3. **Liskov Substitution Principle**: Ensure that child classes (if any) are substitutable for their parent classes without altering the correctness of the program.
4. **Interface Segregation Principle**: Create interfaces that are client-specific rather than large general-purpose interfaces. `InputHandler` might implement an interface with just the `parse_input` method.
5. **Dependency Inversion Principle**: Depend on abstractions rather than implementations. Use dependency injection to pass in `Database` and `InputHandler` instances to TodoCLI.
