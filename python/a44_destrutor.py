class Test:
    def __init__(self, name: str) -> None:
        self.name = name
        print(f"{self.name} - 초기화 되었습니다 ...")
        
    def display_name(self) -> None:
        print(f"현재 이름: {self.name}")

    def change_name(self, new_name: str) -> None:
        # 변경 전 메시지
        print(f"{self.name} - 파괴되었습니다.") 
        self.name = new_name
        # 새 이름 초기화 메시지
        print(f"{self.name} - 초기화 되었습니다 ...")  

def main() -> None:
    names = ["a", "b", "c"]
    instances = [Test(name) for name in names]  # 인스턴스 생성
    
    for instance in instances:
        instance.display_name()  # 각 인스턴스의 이름 출력

    # 이름 변경
    new_names = ["새로운 A", "새로운 B", "새로운 C"]
    for instance, new_name in zip(instances, new_names):
        instance.change_name(new_name)
        instance.display_name()  # 변경된 이름 출력

if __name__ == "__main__":
    # 직접 실행 시_main 함수 호출
    # Call main function when executed directly  
    main()
