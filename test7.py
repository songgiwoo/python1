## 함수 선언 부분 ##
def myFunc():
    print('함수를 호출함.')
def main():
    print('메인 함수 부분이 호출 됩니다')
    myFunc()
    print('전역 변수 값:', gVar)


## 전역 변수 선언 부분 ##
gVar = 100

## 메인 코드 부분 ##
if __name__== '__main__' :
    main()