from abc import ABC, abstractmethod
from IPerson import IRequiredPersonInfo

class Person(IRequiredPersonInfo):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_person_role_in_TEC(self):
        raise NotImplementedError("Subclasses should implement this!")
