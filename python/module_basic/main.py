import test_module as test

def main():
    # 원의 반지름 입력 및 원주 출력
    radius = test.num_input()
    circumference = test.get_circumference(radius)
    print(f"원의 반지름: {radius}, 원의 둘레: {circumference}")
    
    # 직사각형의 폭과 높이 입력 및 면적 출력
    width = test.num_input()
    height = test.num_input()
    rectangle = test.Rectangle(width, height)
    area = rectangle.get_area()
    print(f"직사각형의 면적: {area}")

if __name__ == "__main__":
    main()
