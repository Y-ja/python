class Student:
    count = 0  # 클래스 변수

    def __init__(self, name, kor, eng, math, scien):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.scien = scien
        Student.count += 1  # 학생이 생성될 때마다 count 증가

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
        if isinstance(other, Student):
            return self.total_score() < other.total_score()
        elif isinstance(other, int):
            return self.total_score() < other

    def __le__(self, other: 'Student') -> bool:
        return self.total_score() <= other.total_score()

    def __str__(self) -> str:
        score_sum = self.total_score()
        score_avg = self.average_score()
        return (f"{self.name}\t{score_sum}\t{score_avg:.2f}")

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
    print("이름\t총점\t평균")
    for student in students:
        print(student)

    # 총 학생 수 출력
    print(f"\n총 학생 수: {Student.count}")

if __name__ == "__main__":
    main()
