def main():
    students = [
        {"name": "James", "kor": 87, "eng": 88, "math": 98, "scien": 95},
        {"name": "John", "kor": 85, "eng": 90, "math": 92, "scien": 89},
        {"name": "Michael", "kor": 90, "eng": 85, "math": 94, "scien": 91},
        {"name": "David", "kor": 78, "eng": 82, "math": 88, "scien": 80},
        {"name": "Daniel", "kor": 92, "eng": 87, "math": 90, "scien": 93},
        {"name": "Matthew", "kor": 80, "eng": 79, "math": 85, "scien": 88}
    ]
    
    # 학생 정보 출력
    for student in students:
        score_sum = student['kor'] + student['eng'] + student['math'] + student['scien']
        score_avg = score_sum / 4
        print(f"이름: {student['name']}, 국어: {student['kor']}, 영어: {student['eng']}, 수학: {student['math']}, 과학: {student['scien']}, 합계: {score_sum}, 평균: {score_avg:.2f}")
    

if __name__ == "__main__":
    main()
