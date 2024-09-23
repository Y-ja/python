import math

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius  # 초기화 시 반지름 설정
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter  # 여기에 @radius.setter를 사용합니다.
    def radius(self, value: float) -> None:
        if value < 0:
            raise ValueError("반지름은 0 이상이어야 합니다.")
        self._radius = value
        
    @radius.getter
    def radius(self):
        print("__radius를 요청을 했습니다")
        return self._radius
    
    
    @property
    def circumference(self) -> float:
        return 2 * math.pi * self._radius
    
    @property
    def area(self) -> float:
        return math.pi * self._radius ** 2

def main():
    # Circle 객체 생성
    radius = float(input("반지름을 입력하세요: "))
    circle = Circle(radius)
    
    # 원의 둘레와 넓이 출력
    print(f"원의 둘레: {circle.circumference:.2f}")
    print(f"원의 넓이: {circle.area:.2f}")

if __name__ == "__main__":  
    # Call main function when executed directly
    main()
