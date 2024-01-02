from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


association_table = Table(
     "association_table", Base.metadata,
     Column("student_id", Integer, ForeignKey("student.student_id"), primary_key=True),
     Column("course_id", Integer, ForeignKey("course.course_id"), primary_key=True)
)


class StudentModel(Base):
    __tablename__ = "student"

    student_id = Column("student_id", Integer, autoincrement=True, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    courses_id = relationship("CourseModel", secondary=association_table, back_populates="course_users")

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class CourseModel(Base):
    __tablename__ = "course"

    course_id = Column("course_id", Integer, autoincrement=True, primary_key=True)
    course_name = Column("course_name", String)
    course_description = Column("course_description", String)
    course_users = relationship("StudentModel", secondary=association_table, back_populates="courses_id")

    def __repr__(self):
        return f"{self.course_name} - {self.course_user}"


def get_engine():
    engine = create_engine("postgresql://postgres:vq34v2gx@localhost:5432/postgres", echo=False)
    return engine


def get_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def create_tables():
    Base.metadata.create_all(bind=engine, checkfirst=True)


def create_student(session, first_name, last_name):
    student = StudentModel(first_name=first_name, last_name=last_name)
    session.add(student)
    session.commit()
    return student


def create_course(session, course_name, course_description):
    course = CourseModel(course_name=course_name, course_description=course_description)
    session.add(course)
    session.commit()
    return course


def add_student_to_course(session, student, curse):
    student.courses_id.append(curse)
    session.commit()
    return student


engine = get_engine()
