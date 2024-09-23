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

    def __eq__(self, other: 'Student') -> bool:
        return self.total_score() == other.total_score()

    def __ne__(self, other: 'Student') -> bool:
        return self.total_score() != other.total_score()

    def __gt__(self, other: 'Student') -> bool:
        return self.total_score() > other.total_score()

    def __ge__(self, other: 'Student') -> bool:
        return self.total_score() >= other.total_score()

    def __lt__(self, other: 'Student') -> bool:
        return self.total_score() < other.total_score()

    def __le__(self, other: 'Student') -> bool:
        return self.total_score() <= other.total_score()

    def __str__(self) -> str:
        score_sum = self.total_score()
        score_avg = self.average_score()
        return (f"이름: {self.name}, 국어: {self.kor}, 영어: {self.eng}, "
                f"수학: {self.math}, 과학: {self.scien}, 합계: {score_sum}, "
                f"평균: {score_avg:.2f}")

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
        print(student)

    # 새로운 학생 추가
    new_student = Student("Alex", 87, 82, 73, 84)
    print(new_student)

if __name__ == "__main__":
    main()
