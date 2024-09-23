class Student:
    def __init__(self, name, kor, eng, math, scien):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.scien = scien

    def total_score(self):
        return self.kor + self.eng + self.math + self.scien

    def average_score(self):
        return self.total_score() / 4

def main():
    students = [
        Student("James", 87, 88, 98, 95),
        Student("John", 85, 90, 92, 89),
        Student("Michael", 90, 85, 94, 91),
        Student("David", 78, 82, 88, 80),
        Student("Daniel", 92, 87, 90, 93),
        Student("Matthew", 80, 79, 85, 88)
    ]
    
    # 학생 정보 출력
    for student in students:
        score_sum = student.total_score()
        score_avg = student.average_score()
        print(f"이름: {student.name}, 국어: {student.kor}, 영어: {student.eng}, 수학: {student.math}, 과학: {student.scien}, 합계: {score_sum}, 평균: {score_avg:.2f}")

    # 새로운 학생 추가
    new_student = Student("Alex", 87, 82, 73, 84)
    print(f"이름: {new_student.name}, 국어: {new_student.kor}, 영어: {new_student.eng}, 수학: {new_student.math}, 과학: {new_student.scien}, 합계: {new_student.total_score()}, 평균: {new_student.average_score():.2f}")

if __name__ == "__main__":
    main()
