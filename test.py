# list1 = ["汉堡", "可乐", "薯条"]
# question = input("间隔:")
# answer = question.join(list1)
# print(answer)
# class Test:
#     def __init__(self):
#         self.list1 = [1, 2, 3, 4]
#         self.list2 = [5, 6, 7, 8]
#
#     def listMerge(self, listi):
#         return set(self.list1 + self.list2 + listi)
#
#
# if __name__ == '__main__':
#     hander = Test()
#     list = hander.listMerge([9, 10])
#     print(list)


import ahocorasick


def make_AC(AC, word_set):
    for word in word_set:
        AC.add_word(word, word)
    return AC


def test_ahocorasick():
    '''
    ahocosick：自动机的意思
    可实现自动批量匹配字符串的作用，即可一次返回该条字符串中命中的所有关键词
    '''
    key_list = ["苹果", "香蕉", "梨", "橙子", "柚子", "火龙果", "柿子", "猕猴挑", "赵信", "卡莎"]
    AC_KEY = ahocorasick.Automaton()
    for index, word in enumerate(set(key_list)):
        # print(index, word)
        AC_KEY.add_word(word, word)
    # AC_KEY = make_AC(AC_KEY, set(key_list))
    AC_KEY.make_automaton()
    test_str_list = ["我最喜欢吃的水果有：苹果、梨和香蕉、、、、、德邦", "我也喜欢玩卡莎，吃柚子，但是我不喜欢吃梨"]
    for content in test_str_list:
        name_list = set()
        for item in AC_KEY.iter(content):  # 将AC_KEY中的每一项与content内容作对比，若匹配则返回
            # print(item)  # 返回所在位置和匹配的项
            # print(item[1])
            name_list.add(item[1])
            print(name_list)
        name_list = list(name_list)
        if len(name_list) > 0:
            print(content, "--->命中的关键词有：", "\t".join(name_list))


def list_filtering(l):
    stop_wds = []
    for wd1 in l:
        for wd2 in l:
            if wd1 in wd2 and wd1 != wd2:
                print('这里是wd2:', wd2, '这里是wd1', wd1)
                stop_wds.append(wd1)
    final_wds = [i for i in l if i not in stop_wds]
    return print(stop_wds, '\n', final_wds)


if __name__ == "__main__":
    test_ahocorasick()

    list = ['卡莎', '赵信', '逆羽', '女警', '', '男枪', '卢锡安', '薇恩', '1231']
    list_filtering(list)

    data = {}
    if not data:
        print('1')
    data['args'] = list
    print(data)
