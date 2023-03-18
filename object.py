""" 객체 """
import os
os.system('clear')

#클래스 선언
class Dog:
    name = 'default'
    gender = 'Male/Famale'
    owner = 'default name'

    def Bark(self):
        print(self.name + ': 멍멍')

# 객체 생성과 사용 방법
dog = Dog()
dog.name = "밀크"
dog.name = "Female"
dog.owner = 'S.Heo'
dog.Bark()