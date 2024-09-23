from dataclasses import dataclass

@dataclass
class Student:
    name: str
    kor: int
    eng: int
    math: int
    scien: int

    def total_score(self):
        return self.kor + self.eng + self.math + self.scien

    def average_score(self):
        return self.total_score() / 4

    def print_info(self):
        print(self)  # __str__ 메서드를 호출하여 학생 정보를 출력합니다.

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
        student.print_info()

    # 새로운 학생 추가
    new_student = Student("Alex", 87, 82, 73, 84)
    new_student.print_info()

if __name__ == "__main__":
    main()
