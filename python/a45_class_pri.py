import math

class Circle:
    def __init__(self, radius: float) -> None:
        self.set_radius(radius)  # 초기화 시 반지름 설정
    
    def get_circumference(self) -> float:
        return 2 * math.pi * self._radius
    
    def get_area(self) -> float:
        return math.pi * self._radius ** 2
    
    def get_radius(self) -> float:
        return self._radius
    
    def set_radius(self, radius: float) -> None:
        if radius < 0:
            raise ValueError("반지름은 0 이상이어야 합니다.")
        self._radius = radius

def main():
    # Circle 객체 생성
    radius = float(input("반지름을 입력하세요: "))
    circle = Circle(radius)
    
    # 원의 둘레와 넓이 출력
    print(f"원의 둘레: {circle.get_circumference():.2f}")
    print(f"원의 넓이: {circle.get_area():.2f}")

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    main()
