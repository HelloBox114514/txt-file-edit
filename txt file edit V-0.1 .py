pl=input("请输入txt地址,地址必须存在且文件已创建\n提示：F:/test.txt\n")
print("请选择模式\n[1]阅读txt\n[2]编辑\n")
d=input()
if d=="1":
    with open(pl, encoding='utf-8', mode = "r") as f:
        data = f.read()
        print(data)
if d=="2":
    with open(pl, encoding='utf-8', mode = "r") as f:
        data = f.read()
        print("输入要键入的内容\n直接关闭窗口即可退出")
        for q in range(999999999999999999):
            a = input("")
            with open(pl, encoding='utf-8', mode="a") as f:
                f.writelines(a)
                f.writelines("\n")
