''' 중복이 없는가 : 문자열이 주어졌을 때, 이 문자열에 같은 문자가 중복되어 등장하는지 확인하는 알고리즘을 작성하여라. 자료구조를 추가로 사용하지 않고 풀 수 있는 알고리즘 또한 고민하여라. '''

import collections
# Hash 를 이용
# 딕셔너리.get(key,[default값]) : 딕셔너리에 key가 있으면 해당 key 에 대한 값을 반환하고, 없으면 default에 지정한 값을 반환한다.


def hash(string):
    d = {}

    for w in string:
        d[w] = 0
        # print(d)
    for w in string:
        d[w] += 1
        # print(d)
        if d[w] > 1:
            return True
    return False


print("---------기본--------")
print(hash("heLlo"))


# collections 이용

def hash_collection(string):
    for num in list(collections.Counter(list(string)).values()):
        # print(num)

        if num > 1:
            # print(num)

            return True
    return False


print("---------collections을 이용한 것--------")
print(hash_collection("hello"))
