from Tec import TEC  
from Laerer_module import Teacher  

def main_menu():
    tec = TEC()
    tec.load_from_file("teachers.txt")
    
    while True:
        print("\nMenu:")
        print("1. Opret lærer")
        print("2. Opdater lærer")
        print("3. Vis liste af alle lærere")
        print("4. SAVE and EXIT")
        
        choice = input("Vælg en handling: ")
        
        if choice == '1':
            first_name = input("Indtast fornavn: ")
            last_name = input("Indtast efternavn: ")
            subject = input("Indtast fag: ")
            teacher = Teacher(first_name, last_name, subject)
            tec.add_teacher(teacher)
            print("Lærer oprettet.\n")
        
        elif choice == '2':
            tec.list_teachers()
            try:
                index = int(input("Indtast lærernummer for at opdatere: ")) - 1
                first_name = input("Nyt fornavn: ")
                last_name = input("Nyt efternavn: ")
                subject = input("Nyt fag: ")
                teacher = Teacher(first_name, last_name, subject)
                tec.update_teacher(index, teacher)
                print("Lærer opdateret.\n")
            except (ValueError, IndexError):
                print("Ugyldigt valg. Prøv igen.\n")
        
        elif choice == '3':
            print("\nListe over lærere:")
            tec.list_teachers()
        
        elif choice == '4':
            tec.save_to_file("teachers.txt")
            print("Data gemt. Afslutter programmet.")
            break
        
        else:
            print("Ugyldigt valg. Prøv igen.\n")

if __name__ == "__main__":
    main_menu()
