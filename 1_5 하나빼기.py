''' 하나 빼기 : 문자열을 편집하는 방법에는 세 가지 종류가 있다. 문자 삽입, 문자 삭제, 문자 교체. 문자열 두 개가 주어졌을 때, 문자열을 같게 만들기 위한 편집 횟수가 1회 이내인지 확인하는 함수를 작성하라.'''
# 처음 길이확인한뒤 true, false로 나누고 for문을 나누면 더 나음


def string_edit(before_string, after_string):
    d = {}
    for w in before_string:
        d[w] = 0
    # print(d)
    for w in before_string:
        d[w] += 1
    befor_len = len(d)
    # print(d)
    for w in after_string:
        d[w] = 0
    after_len = len(d)
    # print(d)
    if befor_len == after_len:
        return True
    else:
        if after_len - befor_len in [1, -1]:
            return True
        else:
            return False


print(string_edit("pale", "bake"))
