from datetime import date, timedelta, datetime
from faker import Faker
from random import randint, choice
import sqlite3
from pprint import pprint
from queries import query1, query2, query3, query4, query5, query6, query7, query8, query9, query10, query11, query12
from pprint import pprint

TEACHERS_NUMBER = randint(3, 5)
STUDENTS_NUMBER = randint(30, 50)

subjects = ['Менеджмент',
            'Вища математика',
            "Мікроекономіка",
            "Економічна теорія",
            "Філологія",
            "Іноземна мова",
            "Українська мова",
            "Правознавство",
            ]

fake = Faker('uk-UA')

groups = ['ME-32', "MA-43", 'MO-12']
teachers = [fake.name() for _ in range(TEACHERS_NUMBER)]
students = [fake.name() for _ in range(STUDENTS_NUMBER)]

start_date = datetime.strptime('2022-09-01', '%Y-%m-%d')
end_date = datetime.strptime('2023-05-31', '%Y-%m-%d')

connection = sqlite3.connect('hw.db')
cursor = connection.cursor()

def seed_teachers():
    sql = ("INSERT INTO teachers (fullname) VALUES (?);")
    cursor.executemany(sql, zip(teachers, ))
 
def seed_subjects():
    sql = ('INSERT INTO subjects(name, teacher_id) VALUES (?, ?);')
    cursor.executemany(sql, (zip(subjects, iter(randint(1, TEACHERS_NUMBER) for _ in range(len(subjects))))))

def seed_groups():
    sql = ("INSERT INTO [groups] (name) VALUES (?);")
    cursor.executemany(sql, zip(groups, ))

def seed_students():
    sql = ("INSERT INTO students (fullname, group_id) VALUES (?, ?);")
    
    for s in students:
        group = randint(1, len(groups))
        result = (s, group)
        cursor.execute(sql, result)

def seed_rates():
    dates = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.isoweekday() < 6:
            dates.append(current_date)
        current_date += timedelta(1)
    

    result = start_date - end_date
    sql = "INSERT INTO rates (student_id, subject_id, rate, date_of) VALUES (?, ?, ?, ?);"
    for day in dates:
        subject = randint(1, len(subjects))
        students = [randint(1, STUDENTS_NUMBER) for _ in range(5)]
        for student in students:
            result = (student, subject, randint(1, 12), day.date())
            cursor.execute(sql, result)
    
    
    '''for student_id in range(1, STUDENTS_NUMBER+1):
        for subject_id in range(len(subjects)+1):
            for r in range(20):
                result = (student_id, subject_id, randint(1,12), choice(dates).date())
                cursor.execute(sql, result)'''


def execute_query(sql: str, param) -> list:
    with sqlite3.connect('hw.db') as con:
        cur = con.cursor()
        cur.execute(sql, param)
        return cur.fetchall()
    
if __name__ == '__main__':
    try:
        # наповнюємо БД
        seed_teachers()
        seed_subjects()
        seed_groups()
        seed_students()
        seed_rates()
    except sqlite3.Error as err:
        # перехоплюємо помилки
        print(f"Error happened - {err}")

    finally:
        # перевіряємо чи працюють SQL-команди
        pprint(execute_query(query12,(1, 2)))
        # закриваємо з'єднання
        connection.commit()
        connection.close()