from abc import ABC, abstractmethod


class PersonRepository(ABC):
    
    @abstractmethod
    def add_person(self, person):
        pass