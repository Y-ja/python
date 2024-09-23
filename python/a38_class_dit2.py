def create_student(name, kor, eng, math, scien):
    return {
        "name": name,
        "kor": kor,
        "eng": eng,
        "math": math,
        "scien": scien
    }

def main():
    students = [
        create_student("James", 87, 88, 98, 95),
        create_student("John", 85, 90, 92, 89),
        create_student("Michael", 90, 85, 94, 91),
        create_student("David", 78, 82, 88, 80),
        create_student("Daniel", 92, 87, 90, 93),
        create_student("Matthew", 80, 79, 85, 88)
    ]
    
    # 학생 정보 출력
    for student in students:
        score_sum = student['kor'] + student['eng'] + student['math'] + student['scien']
        score_avg = score_sum / 4
        print(f"이름: {student['name']}, 국어: {student['kor']}, 영어: {student['eng']}, 수학: {student['math']}, 과학: {student['scien']}, 합계: {score_sum}, 평균: {score_avg:.2f}")

if __name__ == "__main__":
    main()
