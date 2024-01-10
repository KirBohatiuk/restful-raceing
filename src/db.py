from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from tenacity import retry, stop_after_delay, stop_after_attempt, wait_fixed
from flask import abort
from .my_utils import get_engine_info

Base = declarative_base()


association_table = Table(
     "association_table", Base.metadata,
     Column("student_id", Integer, ForeignKey("student.id"), primary_key=True),
     Column("course_id", Integer, ForeignKey("course.id"), primary_key=True)
)


class StudentModel(Base):
    __tablename__ = "student"

    id = Column("id", Integer, autoincrement=True, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    courses_id = relationship("CourseModel", secondary=association_table, back_populates="course_users_id")

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class CourseModel(Base):
    __tablename__ = "course"

    id = Column("id", Integer, autoincrement=True, primary_key=True)
    name = Column("name", String)
    description = Column("description", String)
    course_users_id = relationship("StudentModel", secondary=association_table, back_populates="courses_id")

    def __repr__(self):
        return f"{self.course_name} - {self.course_users_id}"


def get_engine():
    db, user, password, host, port, db_name = get_engine_info()
    engine = create_engine(f"{db}://{user}:{password}@{host}:{port}/{db_name}", echo=False)
    return engine


def get_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def create_tables():
    Base.metadata.create_all(bind=engine, checkfirst=True)


@retry(stop=(stop_after_delay(10) | stop_after_attempt(3)), wait=wait_fixed(2))
def create_student(session, first_name, last_name):
    student = StudentModel(first_name=first_name, last_name=last_name)
    session.add(student)
    session.commit()
    return student


@retry(stop=(stop_after_delay(10) | stop_after_attempt(3)), wait=wait_fixed(2))
def get_student(first_name, last_name, session):
    student = session.query(StudentModel).filter(
        StudentModel.first_name == first_name, StudentModel.last_name == last_name
    ).first()
    if not student:
        return abort(404)
    return student


@retry(stop=(stop_after_delay(10) | stop_after_attempt(3)), wait=wait_fixed(2))
def get_all_students(first_name, last_name, session):
    students = session.query(StudentModel).all()
    if not students:
        return abort(404)
    return students


@retry(stop=(stop_after_delay(10) | stop_after_attempt(3)), wait=wait_fixed(2))
def get_course(course_name, session):
    course = session.query(CourseModel).filter(CourseModel.name == course_name).first()
    if course == {}:
        return abort(404)
    return course


@retry(stop=(stop_after_delay(10) | stop_after_attempt(3)), wait=wait_fixed(2))
def get_all_courses(session):
    courses = session.query(CourseModel).all()
    if courses == {}:
        return abort(404)
    return courses


@retry(stop=(stop_after_delay(10) | stop_after_attempt(3)), wait=wait_fixed(2))
def change_student_info(new_name, student, session):
    try:
        student.first_name = new_name["first_name"]
        student.last_name = new_name["last_name"]
        session.commit()
    except:
        return abort(404)
    return student


@retry(stop=(stop_after_delay(10) | stop_after_attempt(3)), wait=wait_fixed(2))
def create_course(session, name, description):
    course = CourseModel(name=name, description=description)
    session.add(course)
    session.commit()
    return course


@retry(stop=(stop_after_delay(10) | stop_after_attempt(3)), wait=wait_fixed(2))
def change_course_info(course_info, course, session):
    try:
        course.name = course_info["course_name"]
        course.description = course_info["course_description"]
        session.commit()
    except:
        return abort(404)
    return course


@retry(stop=(stop_after_delay(10) | stop_after_attempt(3)), wait=wait_fixed(2))
def add_student_to_course(session, student, course):
    student.courses_id.append(course)
    session.commit()
    return student


@retry(stop=(stop_after_delay(10) | stop_after_attempt(3)), wait=wait_fixed(2))
def remove_student_from_course(session, student, course):
    student.courses_id.remove(course)
    session.commit()
    return student


@retry(stop=(stop_after_delay(10) | stop_after_attempt(3)), wait=wait_fixed(2))
def remove_student(session, student):
    session.delete(student)
    session.commit()
    return student


@retry(stop=(stop_after_delay(10) | stop_after_attempt(3)), wait=wait_fixed(2))
def get_student_by_id(student_id, session):
    student = session.query(StudentModel).filter(StudentModel.id == student_id).first()
    if not student:
        return abort(404)
    return student



@retry(stop=(stop_after_delay(10) | stop_after_attempt(3)), wait=wait_fixed(2))
def remove_course(session, course):
    session.delete(course)
    session.commit()
    return course


engine = get_engine()
