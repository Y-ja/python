class Person:
    def __init__(self, name: str):
        self.name = name
    
    def greeting(self):
        print("HELLO")
        
class University:
    def __init__(self, uname: str):
        self.uname = uname
    
    def message_credit(self):
        print("학점_관리")
        
class Undergraduate(Person, University):
    def __init__(self, name: str, uname: str):
        Person.__init__(self, name)
        University.__init__(self, uname)
    
    def study(self):
        print("공부하기")                         
        
def main():
    student = Undergraduate("James", "Korea University") 
    print(student.name, student.uname) 
    
    student.greeting()
    student.message_credit()
    student.study()

if __name__ == "__main__":  
    # 직접 실행 시 main 함수 호출
    # Call main function when executed directly  
    main()
