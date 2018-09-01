class Ab ():
    name = 'Sapurate'
    age = 18
    def hehe(self):
        global age
        age1 = age+1
        print('虚岁为{0}'.format(age1))
        return None

a = Ab()
a.name = 'xzf'
a.age = 20
a.hehe()
