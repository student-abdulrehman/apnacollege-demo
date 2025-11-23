import streamlit as st
from services.storage_service import StorageService
from services.student_manager import StudentManager

from ui.add_student import show_add_student
from ui.update_student import show_update_student
from ui.delete_student import show_delete_student
from ui.list_students import show_list_students
from ui.search_students import show_search_students
from ui.fees_attendance import show_fees_and_attendance

def main():
    st.title("🎓 Student Management System")

    storage = StorageService()
    manager = StudentManager(storage)

    menu = ["Add Student", "Update Student", "Delete Student", "List Students", "Search", "Fees + Attendance"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Student":
        show_add_student(manager)
    elif choice == "Update Student":
        show_update_student(manager)
    elif choice == "Delete Student":
        show_delete_student(manager)
    elif choice == "List Students":
        show_list_students(manager)
    elif choice == "Search":
        show_search_students(manager)
    elif choice == "Fees + Attendance":
        show_fees_and_attendance(manager)

if __name__ == "__main__":
    main()
"Fees + Attendance",
