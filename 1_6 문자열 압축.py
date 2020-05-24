''' 문자열 압축 : 반복되는 문자의 개수를 세는 방식의 기본적인 문자열 압축 메서드를 작성하라. 예를 들어 문자열 aabccccaaa를 압축하면 a2b1c5a3이 된다. 만약 압축된 문자열의 길이가 기존 문자열의 길이보다 길다면 기존 문자열을 반환해야 한다. 문자열은 대소문자 알파벳(a~z)으로만 이루어져있다. '''


def string_zip(string):
    cnt = 0
    len_str = len(string)
    res = ""
    for i in range(len_str):
        cnt += 1

        if i+1 < len_str:
            if string[i] != string[i+1]:
                res += string[i] + str(cnt)
                cnt = 0
        else:
            res += string[i] + str(cnt)

    print(res)
    print(string)

    return res if len_str > len(res) else string


print(string_zip('aabccccaaa'))
# 더 간단한 방법이 있을것 같다
