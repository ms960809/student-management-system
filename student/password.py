# 门禁卡
def password():
    for _ in range(3):
        try:
            n = input('请输入通行证:')
        except:
            print('退出')
            break
        else:
            if n == '123456':
                from student_control.main import main
                main()
                break
            else:
                print('输入密码错误')
if __name__ == '__main__':
    password()
