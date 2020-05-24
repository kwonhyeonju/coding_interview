''' 회문 순열 : 주어진 문자열이 회문의 순열인지 아닌지 확인하는 함수를 작성하라.회문(palindrome)이란 앞으로 읽으나 뒤로 읽으나 같은 단어 혹은 구절을 의미하며, 순열이란 문자열을 재배치하는 것을 뜻한다. 회문이 꼭 사전에 등장하는 단어로 제한될 필요는 없다. '''

# 각각의 문자 모두 짝수개 or 1개 문자만 홀수
# 대소문자 구분함 (문제)


def palin_string(string):
    d = {}
    result = []
    for w in string:
        d[w] = 0
    for w in string:
        d[w] += 1
    for i in range(len(d)):
        result.append(list(d.values())[i] % 2)
    # print(result)
    # print(result.count(1))
    if result.count(1) in [0, 1]:
        return True
    return False


print(palin_string("hello"))
