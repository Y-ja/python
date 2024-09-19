class abc:
    pass
def main():
  print(type(10))
  print(type(object()))
  print(issubclass(str , int))
  print(issubclass(int , object))
  print(issubclass(abc , int))
  print(issubclass(abc , object))

if __name__ == "__main__":    
    main()