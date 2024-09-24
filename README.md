# 📚 Python 소개 🐉🐉🐉🐉🐉🐉🐉🐉

파이썬(Python)은 📈 데이터 분석, 🕹️ 게임 개발, 🌐 웹 개발 등 다양한 분야에서 널리 사용되는 고급 프로그래밍 언어입니다. 쉽고 간결한 문법 덕분에 초보자부터 전문가까지 모두에게 적합합니다.
## 🔑 주요 특징

- 가독성: 📝 명확하고 간결한 문법으로 코드가 읽기 쉽습니다.
- 다양한 라이브러리: 📦 풍부한 라이브러리와 프레임워크가 있어 다양한 작업을 쉽게 수행할 수있습니다.
- 플랫폼 독립성: 💻 다양한 운영체제에서 실행 가능하여 유연성이 뛰어납니다.
- 대화형 프로그래밍: 🖥️ REPL(Read-Eval-Print Loop) 환경을 통해 즉시 실행 및 테스트가 가능합니다.

## 🚀 시작하기

- 설치하기: Python 공식 웹사이트(https://www.python.org) 에서 다운로드하여 설치하세요.
    python
```
print("안녕하세요, 파이썬!")
```
- IDE 추천:
```
    🖥️ PyCharm
    📘 Visual Studio Code
    🐍 Jupyter Notebook
```
## 📚 파이썬 기초 키워드 정리
1. 키워드 (Keywords) 🗝️
파이썬의 예약어로, 특별한 의미를 갖는 단어입니다. 예: if, for, while, def 등.

2. 이름 (Name) 🏷️
변수, 함수, 클래스 등의 이름을 정의하는 데 사용합니다. 명확하고 의미 있는 이름을 사용하는 것이 좋습니다. 

3. 변수 (Variable) 📦

데이터를 저장하는 데 사용되는 이름이 있는 공간입니다
```
x = 10  # x라는 변수에 10을 저장

```
4. 연산자 (Operator) ➕➖
값을 조작하는 데 사용되는 기호입니다. 

    - 산술 연산자: +, -, *, /
    - 비교 연산자: ==, !=, <, >

5. 출력 (Print) 🖨️
콘솔에 내용을 표시하는 데 사용됩니다.
```
print("안녕하세요, 파이썬!")

```

6. 데이터 (Data) 📊
변수에 저장된 정보로, 다양한 형식을 가질 수 있습니다. 예: 숫자, 문자열, 리스트 등.

7. 문자열 인덱싱 (Str Indexing) 🔍
문자열의 각 문자는 인덱스를 사용하여 접근할 수 있습니다. 인덱스는 0부터 시작합니다. 
```
my_string = "안녕하세요"
print(my_string[0])  # '안'

```
8. 데이터 타입 (Datatype) 🧩

변수에 저장된 데이터의 종류를 나타냅니다. 

    - 정수형 (int) 📏
    - 실수형 (float) 📐
    - 문자열 (str) 📝
    - 불리언 (bool) 🔳

9. 길이 (Length) 📏

문자열, 리스트 등의 길이를 반환하는 함수입니다. len() 함수를 사용합니다.
```
my_list = [1, 2, 3]
print(len(my_list))  # 3
```

## 2024.09.20
### 📋 리스트 (List)
- 여러 값을 저장할 수 있는 순서가 있는 컬렉션입니다.
```
my_list = [1, 2, 3, 4, 5]
```
- 주요 메서드
- append(value): 리스트의 끝에 값을 추가
- remove(value): 첫 번째로 발견된 값을 삭제
- pop(index): 지정된 인덱스의 값을 삭제하고 반환

### 🔄 range for문
- 특정 범위의 숫자들을 생성하는 함수.
```
    for i in range(5):
        print(i)  # 0, 1, 2, 3, 4
```
- 파라미터
- start: 시작 값 (기본값 0)
- stop: 종료 값 (미포함)
- step: 증가 값 (기본값 1)

### 📚 딕셔너리 (Dictionary)
- 키-값 쌍으로 데이터를 저장하는 컬렉션입니다.
```
    my_dict = {'key1': 'value1', 'key2': 'value2'}
```
- 주요 메서드
- get(key): 키에 해당하는 값을 반환 (존재하지 않으면 None)
- keys(): 모든 키를 반환
- values(): 모든 값을 반환

### 🔄 딕셔너리 for문
```
    for key, value in my_dict.items():
        print(key, value)
```

### ⏳ while문
- 조건이 참인 동안 반복하는 루프입니다.
```
    count = 0
    while count < 5:
        print(count)
        count += 1
```
### 📋 리스트 메서드 (List Methods)
- extend(iterable): 리스트에 다른 iterable을 추가
- insert(index, value): 지정된 인덱스에 값을 삽입
- sort(): 리스트를 정렬

### 📖 딕셔너리 메서드 (Dictionary Methods)
- update(other): 다른 딕셔너리의 키-값 쌍으로 업데이트
- popitem(): 마지막으로 추가된 키-값 쌍을 삭제하고 반환

## 2024_09_23

### 01. 클래스 개념 🏷️
클래스는 객체 지향 프로그래밍의 기본 단위로, 데이터와 메서드를 묶어 새로운 데이터 타입을 정의합니다.

```python
class Dog:
    def bark(self):
        return "Woof!"
```

## 02. 파이썬 데이터 처리 (간단한 클래스, dataclass 디코레이터) 💻

- 간단한 클래스: 사용자 정의 데이터 구조를 만드는 방법.
- dataclass 디코레이터: 데이터 클래스를 간편하게 정의하고 기본 메서드를 자동으로 생성합니다.

```
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

```

## 03. 메서드 추가 ➕
클래스에 다양한 메서드를 추가하여 기능을 확장하는 방법을 설명합니다.
```
class Calculator:
    def add(self, a, b):
        return a + b

```

## 04. 스페셜 메서드 추가 ✨

__init__, __str__, __repr__ 등의 스페셜 메서드를 활용하여 클래스의 동작을 정의합니다.

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

```

## 05. 클래스 변수 활용 (dataclass 디코레이터) 📊
클래스 변수와 인스턴스 변수를 구분하고 활용하는 방법을 다룹니다.

```
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

```

## 06. private 설정 🔒
변수를 비공개로 설정하여 외부에서 접근하지 못하도록 보호하는 방법을 설명합니다.

```
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def get_balance(self):
        return self.__balance

```
## 07. property 디코레이터 (getter, setter) 🔍
@property를 사용하여 속성을 제어하고, getter/setter 메서드를 만드는 방법을 설명합니다.

```
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

```

## 08. 재귀 함수 (lru_cache 디코레이터, tuple exchange) 🔄
재귀 함수의 개념과 functools.lru_cache를 활용하여 성능을 향상시키는 방법을 다룹니다.

```
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

```

## 09. lambda 함수 (파일 처리, 랜덤 모듈, 제너레이터) 🔄
람다 함수의 활용 예제와 함께 파일 처리 및 제너레이터를 소개합니다.

```
import random

random_numbers = list(map(lambda x: x * 2, range(10)))
print(random_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

```

## 2024_09_24

## 모듈 개념 📦
모듈은 관련된 함수와 클래스를 하나의 파일로 묶어 재사용할 수 있도록 합니다. 다른 파일에서 모듈을 불러와 기능을 확장할 수 있습니다.

```
# my_module.py
def greet(name):
    return f"Hello, {name}!"

# main.py
from my_module import greet

print(greet("Alice"))  # Hello, Alice!

```

## 패키지 개념 📂

패키지는 관련된 여러 모듈을 하나의 디렉터리로 묶는 방법입니다. 패키지를 통해 모듈의 구조를 정리할 수 있습니다.

```
my_package/
    __init__.py
    module1.py
    module2.py

```

## import 개념 📥

다른 모듈이나 패키지를 사용할 때는 import 문을 사용합니다. 이를 통해 외부 기능을 쉽게 활용할 수 있습니다.

```
import my_module  # 모듈 전체를 임포트
from my_module import greet  # 특정 함수만 임포트

```
## __init__.py 개념 📝

패키지를 정의하는 파일로, 패키지를 임포트할 때 실행됩니다. 이 파일이 존재해야 Python은 디렉터리를 패키지로 인식합니다.

```
# __init__.py
print("my_package가 임포트되었습니다!")

```