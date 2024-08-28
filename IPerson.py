from abc import ABC, abstractmethod

class IRequiredPersonInfo(ABC):
    @abstractmethod
    def get_full_name(self):
        pass

    @abstractmethod
    def get_person_role_in_TEC(self):
        pass
