from Laerer_module import Teacher

class TEC:
    def __init__(self):
        self.teachers = []
    
    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)
    
    def update_teacher(self, index: int, teacher: Teacher):
        if 0 <= index < len(self.teachers):
            self.teachers[index] = teacher
    
    def list_teachers(self):
        if not self.teachers:
            print("No teachers registered.")
        for idx, teacher in enumerate(self.teachers, start=1):
            print(f"{idx}. {teacher}")
    
    def save_to_file(self, filename: str):
        with open(filename, 'w') as f:
            for teacher in self.teachers:
                f.write(f"{teacher.first_name},{teacher.last_name},{teacher.subject}\n")
    
    def load_from_file(self, filename: str):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    first_name, last_name, subject = line.strip().split(',')
                    self.add_teacher(Teacher(first_name, last_name, subject))
        except FileNotFoundError:
            print(f"No existing data found. Starting fresh.")
