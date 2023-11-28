from abc import ABC, abstractmethod

class CommandInterface(ABC):
    @abstractmethod
    def execute(self, args, db, formatter):
        pass