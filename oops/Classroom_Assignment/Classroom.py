class Classroom:
    Classroom_list=["C1A","C2A","C3A"]
    @staticmethod
    def search_classroom(class_room):
        if class_room in Classroom.Classroom_list:
            print(f"class room {class_room} is Found")
        else:
            print(f"class room {class_room} is NotFound")

Classroom.search_classroom("C1A")
Classroom.search_classroom("C2A")
Classroom.search_classroom("C3A")
Classroom.search_classroom("C4A")
