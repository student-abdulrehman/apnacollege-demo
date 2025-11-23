from models.student import Student
s = Student.create('Test Student', 15, 'A', 85)
print('OK', s.total_fee, s.id)
