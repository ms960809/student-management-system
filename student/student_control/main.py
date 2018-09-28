from student_control.student_info import *
# 定义选项函数
def main():
    # 以下代码为选择界面
    l = []
    while 1:
        from menu import show_menu
        show_menu()
        try:
            choice_l = input('请选择：')
        except:
            print('退出')
            break
        else:
            if choice_l == 'q':
                print('您已退出学生信息管理系统！欢迎下次光临！')
                break
            else:
                if choice_l.isdigit():
                    choice_l = int(choice_l)
                    if choice_l == 1:
                        try:
                            l += input_student()
                        except KeyboardInterrupt:
                            print('退出')
                            break
                    elif choice_l == 2:
                        if len(l) == 0:
                            print('信息为空')
                        else:
                            output_student(l)
                    elif choice_l == 3:
                        if len(l) == 0:
                            print('信息为空')
                            pass
                        else:
                            try:
                                delete_student(l)
                                output_student(l)
                            except:
                                print('退出')
                                break
                    elif choice_l == 4:
                        if len(l) == 0:
                            print('信息为空')
                        else:
                            try:
                                change_student(l)
                                output_student(l)
                            except:
                                print('退出')
                                break
                    elif choice_l == 5:
                        if len(l) == 0:
                            print('信息为空')
                        else:
                            s = score_high_student(l)
                            output_student(s)
                    elif choice_l == 6:
                        if len(l) == 0:
                            print('信息为空')
                        else:
                            s = score_di_student(l)
                            output_student(s)   
                    elif choice_l == 7:
                        if len(l) == 0:
                            print('信息为空')
                        else:
                            s = age_high_student(l)
                            output_student(s)
                    elif choice_l == 8:
                        if len(l) == 0:
                            print('信息为空')   
                        else:
                            s = age_di_student(l)
                            output_student(s)
                    elif choice_l == 9:
                        cc(l)
                    elif choice_l == 0:
                        l = xs()
                    else:
                        print('输入的数字范围不对')
                else:
                    print('如果您想退出，请按ｑ，否则请输入数字')
