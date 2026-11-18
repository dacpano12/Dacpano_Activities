class Student:
    # Step 1 & 2: Attributes + Constructor
    def __init__(self, name, student_id, grade):
        self.__name = name        # private
        self.__student_id = student_id  # private
        self.__grade = grade      # private

    # Step 3: Getters
    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id

    def get_grade(self):
        return self.__grade

    # Setter — only for grade
    def set_grade(self, new_grade):
        self.__grade = new_grade

    # Step 4: displayInfo() method
    def display_info(self):
        print(f"Name: {self.__name} | ID: {self.__student_id} | Grade: {self.__grade:.1f}")


# Step 5: Main program
if __name__ == "__main__":
    # Create two Student objects
    student1 = Student("Juan Dela Cruz", "2026-001", 92.0)
    student2 = Student("Maria Santos", "2026-002", 85.0)

    # Change one student's grade
    student2.set_grade(88.5)

    # Display both
    student1.display_info()
    student2.display_info()
