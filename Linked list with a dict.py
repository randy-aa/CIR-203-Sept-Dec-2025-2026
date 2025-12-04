class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, name, admission_no, grades):
        student_dict = {
            "Name": name,
            "Admission_No": admission_no,
            "Grades": grades
        }
        new_node = Node(student_dict)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            student = current.data
            grades_str = ", ".join([f"[{course}-{mark}]" for course, mark in student["Grades"]])
            print(f"Name: {student['Name']} | Admission No: {student['Admission_No']} | Grades: {grades_str}")
            current = current.next


# Example usage with your three admission numbers
students = LinkedList()
students.insert("Alice", "CIM/00095/024", [("CIR 205", 85), ("CIR 203", 80), ("CIS 221", 91)])
students.insert("Bob", "CIM/00066/024", [("CIR 205", 75), ("CIR 203", 70), ("CIS 221", 82)])
students.insert("Charlie", "CIM/00128/024", [("CIR 205", 95), ("CIR 203", 89), ("CIS 221", 92)])

students.display()
