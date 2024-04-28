

from  person import Person
from person_repository import PersonRepository

class PersonService:
    
    def __init__(self, repository):
        self.repository = repository
        
    def create_person(self, person_data):
        person_ = Person(person_data)
        return self.repository.add_person(person_)
        
        
        
if  __name__ == "__main__":
    PersonService()