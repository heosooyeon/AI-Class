""" 가변인자, 키워드인자 """
# *arguments는 가변인자(variable argument) : 별 한개면 리스트
# **keywords는 키워드인자(Keyword arguments) : 별 두개면 딕셔너리
def caffe(beverage, *arguments, **keywords):
    print("Do you have any", beverage, "?")
    for arg in arguments:
        print(arg)
    print("*****")
    for kw in keywords:
        print(kw, ":", keywords[kw])

caffe("coffee","it's yummy, sir.","World you try?",
      barista = "Soo yeon",
      client = "BSSM",
      cup = "Venti-size"
      )
