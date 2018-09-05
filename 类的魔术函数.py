class Ok():
    def __init__(self, name):
        self.name = name

    # __gt__函数是一个典型的魔术函数，用来比较大小
    def __gt__(self, obj):
        print("{0}会比{1}大吗？".format(self.name, obj.name))
        if (self.name > obj.name):
            print("---这是肯定的！")
        else:
            print("---显然不可能！")

str1 = Ok("yop")
str2 = Ok("str2")
str1 > str2