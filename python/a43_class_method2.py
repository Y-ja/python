class Student:
    count = 0  # 클래스 변수
    students = []  # 학생 목록을 저장할 클래스 변수

    def __init__(self, name, kor, eng, math, scien):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.scien = scien
        Student.increment_count()  # 학생이 생성될 때마다 count 증가
        Student.students.append(self)  # 생성된 학생을 리스트에 추가

    @classmethod
    def increment_count(cls):
        cls.count += 1  # 클래스 변수 증가

    @classmethod
    def print_students(cls):
        print("이름\t총점\t평균")
        for student in cls.students:
            print(f"{student.name}\t{student.total_score()}\t{student.average_score():.2f}")

    def total_score(self):
        return self.kor + self.eng + self.math + self.scien

    def average_score(self):
        return self.total_score() / 4

def main():
    # 학생 생성
    Student("James", 87, 88, 98, 95)
    Student("John", 85, 90, 92, 89)
    Student("Michael", 90, 85, 94, 91)
    Student("David", 78, 82, 88, 80)
    Student("Daniel", 92, 87, 90, 93)
    Student("Matthew", 80, 79, 85, 88)

    # 학생 정보 출력
    Student.print_students()

    # 총 학생 수 출력
    print(f"\n총 학생 수: {Student.count}")

if __name__ == "__main__":
    main()
