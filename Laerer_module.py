from Person import Person

class Laerer(Person):
    def __init__(self, first_name, last_name, subject):
        super().__init__(first_name, last_name)
        self.subject = subject

    def get_person_role_in_TEC(self):
        return "Lærer"

    def get_subject(self):
        return self.subject

    def __str__(self):
        return f"{self.get_full_name()} - {self.subject}"
