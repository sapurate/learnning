class Stu():
    def __init__(self,name="NoName",age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}!".format(self.name))

def sayhello():
    print("你们好呀！")

if __name__ == '__main__':

    print("不要运行我！")