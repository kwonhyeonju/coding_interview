'''순열 확인 : 문자열 두개가 주어졌을 때 이 둘이 서로 순열 관계에 있는지 확인하는 메서드를 작성하라. '''

# 문자열 둘다 정렬 후 비교


def string_sort(string1, string2):
    s1 = sorted(string1)
    s2 = sorted(string2)
    if s1 == s2:
        return "일치합니다."
    else:
        return "일치하지 않습니다."


print(string_sort("hello", "horel"))
