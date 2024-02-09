#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import Column, DateTime, func, Integer, desc, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.grade}"

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()


    albert_einstein = Student(
        name="Albert Einstein",
        email="albert.einstein@zurich.edu",
        grade=6,
        birthday=datetime(
            year=1879,
            month=3,
            day=14
        ),
    )



    Jeff_Fitzpatrick = Student(
        name="Jeff Fitzpatrick",
        email="jeff.fitzpatrick@jeffsemail.com",
        grade=42,
        birthday=datetime(
            year=1976,
            month=1,
            day=17
        ),
    )

    #session.add(albert_einstein)
    #session.add(Jeff_Fitzpatrick)
    session.bulk_save_objects([albert_einstein, Jeff_Fitzpatrick])
    session.commit()

    #students = session.query(Student)

#print([student for student in students])

    students = session.query(Student.name).all()
    all =[]
    for i in range(len(students)):
        print(f"{students[i]}")
    print(students)
        
    
  
    students_by_name = session.query(
        Student.name).order_by(
        Student.name).all()

    students_by_grade_desc = session.query(
        Student.name, Student.grade).order_by(
        desc(Student.grade)).all()

    oldest_student = session.query(
        Student.name, Student.birthday).order_by(
        Student.birthday).limit(1).all()

   
    oldest_student = session.query(
        Student.name, Student.birthday).order_by(
        Student.birthday).first()

    print(oldest_student)


    student_count = session.query(func.count(Student.id)).first()

    print(student_count)

    query = session.query(Student).filter(Student.name.like('%Jeff%'),
        Student.grade == 42).all()

    for record in query:
        print(record.name)

    #update


        # create session, student objects

    for student in session.query(Student):
        student.grade += 1

    session.commit()

    print([(student.name,
        student.grade) for student in session.query(Student)])

    session.query(Student).update({
    Student.grade: Student.grade + 1
    })

    print([(
        student.name,
        student.grade
    ) for student in session.query(Student)])




    ###################deleting data ################################


   # print(students_by_name)
   # print(students_by_grade_desc)


    query = session.query(
        Student).filter(
            Student.name == "Albert Einstein")

    # retrieve first matching record as object
    albert_einstein = query.first()

    # delete record
    session.delete(albert_einstein)
    session.commit()

    # try to retrieve deleted record
    albert_einstein = query.first()

    print(albert_einstein)



#print(f"New student ID is {albert_einstein.id}.")
