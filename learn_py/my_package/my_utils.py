def print_file(filename):
    f = None
    try:
        f = open(filename,"r",encoding="utf-8")
        content = f.read()
        print("文件的全部内容是：")
        print(content)
    except Exception as e:
        print(f"程序出现错误，{e}")
    finally:
        if f:
            f.close()

# def print_file(filename):
#     try:
#         with open(filename, "r", encoding="utf-8") as f:  # 自动管理文件
#             content = f.read()
#             print("文件的全部内容是：")
#             print(content)
#     except Exception as e:
#         print(f"读取文件时发生错误: {e}")


if __name__ == "__main__":
    print_file("D:/test_py.txt")