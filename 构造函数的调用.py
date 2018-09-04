class People():
    def __init__(self,name,age):
        self.name = name.upper()
        self.age = age
    def js(self):
        print("我的名字叫{0}，我今年{1}岁了！".format(self.name,self.age))

a = People(name="Sapurate",age=18)
a.js()