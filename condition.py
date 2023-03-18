""" if조건문 """
import os
os.system('clear')

num = int(input("정수형 숫자를 입력하세요 : "))
if num < 0:
    num = 0
    print('음수라서 0으로 설정')
elif num == 0:
    print('0입니다.')
elif num == 1:
    print("1입니다.")
else :
    print('1보다는 큽니다.')