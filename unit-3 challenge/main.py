class student:
  def __init__(self,name,roll_number,cgpa):
   self.name=name
   self.roll_number=roll_number
   self.cgpa=cgpa
  def sorted_student(student_list):
    sorted_students=sorted(student_list,
                       key:lamba student:student.cgpa,
                            reverse=true)
    return sorted_students

students=[
  student("hari","A123",7.9),
  student("abi","A124",8.1),
  student("jeeve","A125",9.1)
]
sorted_students=sorted_students(students)
for student in  sorted_students:
  print("name:{},roll_number;{},cgpa:{}".format(student.name,student,roll_number))