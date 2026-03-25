def calculator():
    print("欢迎使用计算器！")
    
    while True:
        # 获取用户输入的第一个数字
        try:
            num1 = float(input("请输入第一个数字: "))
        except ValueError:
            print("请输入有效的数字！")
            continue
        
        # 获取用户输入的运算符
        operator = input("请输入运算符 (+, -, *, /): ")
        if operator not in ['+', '-', '*', '/']:
            print("请输入有效的运算符！")
            continue
        
        # 获取用户输入的第二个数字
        try:
            num2 = float(input("请输入第二个数字: "))
        except ValueError:
            print("请输入有效的数字！")
            continue
        
        # 执行计算
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("错误：除数不能为零！")
                continue
            result = num1 / num2
        
        # 显示结果
        print(f"结果: {num1} {operator} {num2} = {result}")
        
        # 询问用户是否继续
        again = input("是否继续计算？ (y/n): ")
        if again.lower() != 'y':
            print("感谢使用计算器，再见！")
            break

if __name__ == "__main__":
    calculator()