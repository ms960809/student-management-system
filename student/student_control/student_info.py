from student_control.student import Student
# 输入学生信息
def input_student():
    l = []
    while 1:
        pass
        n = input('请输入学生姓名:')
        if n == '':
            break
        try:
            a = int(input('请输入学生年龄:'))
            s = int(input('请输入学生成绩:'))
            st = Student(n,a,s)
            l.append(st)
        except :
            print('输入有误')
    return l
# 检测名字中的中文
def get_chinese(n):
    i = 0
    for y in n:
        if ord(y) > 127:
            i += 1
    return i
# 定义函数打印出录入学生的信息
def output_student(l):
    # 打印学生信息列表
    print('+'+'-' * 20  + '+' +\
            '-' * 10 + '+' + '-' * 10 + '+')
    print('|'+'name'.center(20) +'|'+'age'.center(10) + '|'\
            + 'score'.center(10) + '|')
    print('+'+'-' * 20 + '+' + '-' * 10 + '+' + \
            '-' * 10 + '+')
    for x in l:
        n,a,s = x.get_info()
        i = get_chinese(n)
        b = '|' + n.center(20 - i) + '|' + \
            str(a).center(10)\
            + '|'+ str(s).center(10) + '|'
        print(b)
    print('+'+'-' * 20+ '+' + '-' * 10 + '+' +\
            '-' * 10 + '+')
    return ''
#定义删除学生信息的函数
def delete_student(l):
    delete = input('请输入要删除的信息:')
    for d in l:
        n,a,s = d.get_info()
        if n == delete:
             l.remove(d)
             print('删除成功')
             break
    else:
        print('没有这个信息')
    return l
#定义修改信息的函数
def change_student(l):
    change = input('请输入要修改的学生信息:')
    for d in l:
        n,a,s = d.get_info()
        if n == change:
            change_name = input('请输入修改后的姓名:') or '0'
            change_age = input('请输入修改后的年龄:') or '0'
            change_score = input('请输入修改后的成绩:') or '0'
            if change_name == '0':
                pass
            else:
                n = change_name
            if change_age == '0':
                pass
            else:
                a = change_age
            if change_score == '0':
                pass
            else:
                s = change_score
            l.remove(d)
            l.append(Student(n,a,s))
            print('修改成功')
            break
    else:
        print('没有该信息')
    return l
# 以成绩从高到低排序
def score_high_student(l):
    l = sorted(l,key = lambda d:d.get_score(),reverse = True)
    return l
# 以成绩从低到高排序
def score_di_student(l):
    l = sorted(l,key = lambda d:d.get_score())
    return l
# 以年龄从低到高排序
def age_di_student(l):
    l = sorted(l,key = lambda d:d.get_age(),)
    return l
# 以年龄从高到低排序
def age_high_student(l):
    l = sorted(l,key = lambda d : d.get_age(),reverse =True)
    return l
# 保存信息到文件
def cc(l):
    try:
        f = open('is.txt','wt')
        for i in l:
            i.save(f)
        f.close()
        print('保存成功')
    except:
        print('写文件失败')
# 从文件中读取信息
def xs(filename = 'is.txt'):
    l = []
    try:
        f = open(filename)
        for line in f:
            n,a,s = line.strip().split('\t')
            a = int(a)
            s = int(s)
            l.append(Student(n,a,s))
        print('读取成功')
    except:
        print('读取失败')
    return l