'''
定义一个学生类,用来形容学生
'''
# 定义一个空的类
class Student():
    pass
# 定义一个对象
mingyue = Student()
class PythonStudent():
    name = None
    age = 18
    course = "Paython"
    def doHomeWord(self):
        print("跑步呢")
        return None
yueyue = PythonStudent()
print(yueyue.age)
print(yueyue.name)
yueyue.doHomeWord()