from services.storage_service import StorageService
from services.student_manager import StudentManager
from models.student import Student

s = StorageService()
manager = StudentManager(s)
print('Initial count:', len(manager.list_students()))

# Add a student
st = Student.create('Automated Test', 12, 'B', 88.5, total_fee=3000)
manager.add_student(st)
print('After add:', len(manager.list_students()))

# Update student
ok = manager.update_student(st.id, grade='A', performance=90)
print('Update ok:', ok, 'now grade:', manager.get_student(st.id).grade)

# Add payment
okp = manager.add_payment(st.id, 500, 'Cash', '2025-11-23')
print('Payment ok:', okp, 'amount_paid:', manager.get_student(st.id).amount_paid)

# Mark attendance
oka = manager.mark_attendance(st.id, '2025-11', 23, 'P')
print('Mark attendance ok:', oka, 'attendance:', manager.get_month_attendance(st.id, '2025-11'))

# Search
res = manager.search(name='Automated')
print('Search results:', len(res))

# Delete
delok = manager.delete_student(st.id)
print('Delete ok:', delok, 'final count:', len(manager.list_students()))
