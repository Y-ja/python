PI = 3.1415926535

def num_input():
    """사용자로부터 숫자를 입력받아 반환합니다."""
    output = input("숫자 입력 -> ")
    return float(output)

def get_circumference(radius):
    """주어진 반지름에 대해 원의 둘레를 계산하여 반환합니다."""
    return 2 * PI * radius  # 원주율에 반지름을 곱하여 원주를 계산합니다.

class Rectangle:
    def __init__(self, w, h) -> None:
        """폭과 높이를 받아 직사각형 객체를 초기화합니다."""
        self.width = w  # 폭
        self.height = h  # 높이
    
    def get_area(self):
        """직사각형의 면적을 계산하여 반환합니다."""
        return self.width * self.height  # 면적 계산

