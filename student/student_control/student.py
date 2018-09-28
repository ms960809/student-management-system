'''此模块用于定义一个学生类，次类用于生成学生对象，来存除学生相关信息'''
class Student:
    def __init__(self,n,a,s):
        if 0 <= int(a) <= 150 and 0 <= int(s) <= 150:
            self.__name,self.__age,self.__score = n,a,s
        else:
            print('成绩或者年龄不合法')
    def get_info(self):
        '''此方法用来返回学生信息的元组'''
        return (self.__name,self.__age,self.__score)
    def get_score(self):
        return self.__score
    def get_age(self):
        return self.__age
    def save(self,file):
        file.write(self.__name)
        file.write('\t')
        file.write(str(self.__age))
        file.write('\t')
        file.write(str(self.__score))
        file.write('\n')