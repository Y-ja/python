class abc:
    def __getitem__(self , idx):
        return idx

def main():
    print("문자 연산자에 알아 볼까요?")
    print("Hello_"[0])
    print("Hello_"[1])
    print("Hello_"[2])
    print("Hello_"[3])
    print("Hello_"[4])
    print("Hello_"[5])
    a = abc()
    print(a[3])
     ## 이외는 out of range 
    print("Hello_"[-1])
    print("Hello_"[-2])
    print("Hello_"[-3])
    print("Hello_"[-4])
    print("Hello_"[-5])
   
    print("안녕하세욥!!!"[1:4])
    print("안녕하세욥!!!"[1:4:1])
    print("안녕하세욥!!!"[1:4:2])
    print("안녕하세욥!!!"[::-1])
    
if __name__ == "__main__":
    main()