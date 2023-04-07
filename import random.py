import random
from tarfile import PAX_NUMBER_FIELDS
import time

# 定义题目生成函数
def generate_question(max_num):
    num1 = random.randint(1, max_num)
    num2 = random.randint(1, max_num)
    return num1, num2

# 定义答题函数
def answer_question(num1, num2, timeout):
    start_time = time.time()  # 记录答题开始时间
    result = input(f"{num1} × {num2} = ")
    end_time = time.time()  # 记录答题结束时间
    used_time = end_time - start_time  # 计算答题用时
    if used_time > timeout:  # 如果答题用时超过规定时间，则判定为答错
        return False, used_time
    elif int(result) == num1 * num2:  # 如果答案正确，则返回True和用时
        return True, used_time
    else:  # 否则判定为答错
        return False, used_time

# 定义回溯函数，返回总分和错题列表
def backtrack(scores, wrongs, index, path, max_index):
    if index == max_index:  # 如果遍历完所有题目，则返回总分和错题列表
        return sum(scores), wrongs
    else:
        score, used_time = scores[index]
        if score == 0:  # 如果这道题答错了
            print(f"第{index+1}题答错了，用时{used_time:.2f}秒。")
            while True:  # 循环直到用户输入正确的选项
                option = input("请选择：退出（Q）、重来（R）、跳过（S）")
                if option == "Q":
                    return sum(scores), wrongs
                elif option == "R":
                    scores[index] = (0, 0)  # 把这道题分数清零
                    path.append(index)  # 把这道题的编号加入回溯路径
                    return backtrack(scores, wrongs, index, path, max_index)  # 回溯到上一题
                elif option == "S":
                    scores[index] = (1, 0)  # 把这道题的分数改为1
                    return backtrack(scores, wrongs, index+1, path, max_index)  # 继续做下一题
                else:
                    print("无效选项，请重新选择。")
        else:  # 如果这道题答对了
            return backtrack(scores, wrongs, index+1, path, max_index)  # 继续做下一题

# 定义主函数
def main():
    max_num = 100  # 最大乘数
    easy_timeout = 30  # 简单难度的答题时间
    normal_timeout = 60  # 普通难度的答题时间
    hard_timeout = 30  # 困难难度的答题时间
    num_of_questions = 20  # 每次练习的题目数

# 定义登录函数
def login():
    # 这里省略了登录功能的实现，可以自行补充
    # 如果登录成功，返回用户名
    return "test_user"

username = login()  # 调用登录函数，获取用户名

# 定义练习函数
def practice(difficulty):
    # 生成难度对应的答题时间
    if difficulty == "easy":
        timeout = easy_timeout= 30
    elif difficulty == "normal":
        timeout = normal_timeout = 60
    else:
        timeout = hard_timeout = 30

    # 生成题目
    questions = [generate_question(PAX_NUMBER_FIELDS) for i in range(num_of_questions)]
    scores = [(0, 0) for i in range(num_of_questions)]  # 初始化得分数组
    for i, question in enumerate(questions):
        print(f"第{i+1}题：")
        while True:  # 循环直到用户输入正确的选项
            result, used_time = answer_question(question[0], question[1], timeout)
            if result:  # 如果答案正确，则记录得分和用时
                scores[i] = (1, used_time)
                break
            else:  # 否则提示答案错误
                print("答案错误，请重新作答。")

    # 计算总分
    total_score = sum([score[0] for score in scores])
    print(f"您的总得分为{total_score}分。")

    # 如果有错题，调用回溯函数，输出错题列表
    wrongs = []
    for i, score in enumerate(scores):
        if score[0] == 0:
            wrongs.append(i)
    if wrongs:
        print("您的错题列表如下：")
        total_score, wrongs = backtrack(scores, wrongs, 0, [], num_of_questions)
        print(f"您的总得分为{total_score}分。")
        for i in wrongs:
            print(f"第{i+1}题")

# 定义查看成绩函数
def view_scores():
    # 这里省略了查看成绩功能的实现，可以自行补充
    # 如果查询成功，返回得分数组
    return [(1, 10), (1, 12), (0, 31), (1, 9), (1, 11)]

while True:  # 循环直到用户选择退出
    option = input("请选择：练习（P）、查看成绩（S）、退出（Q）")
    if option == "P":
        difficulty = input("请选择难度：简单（E）、普通（N）、困难（H）")
        practice(difficulty.lower())
    elif option == "S":
        scores = view_scores()
        total_score = sum([score[0] for score in scores])
        print(f"您的总得分为{total_score}分。")
        for i, score in enumerate(scores):
            print(f"第{i+1}次练习得分为{score[0]}分，用时{score[1]}秒。")
    else:
        break

print("谢谢使用，再见！")


