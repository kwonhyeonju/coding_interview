''' URL화 : 문자열에 들어 있는 모든 공백을 '%20'으로 바꿔 주는 메서드를 작성하라. 최종적으로 모든 문자를 다 담을 수 있을 마늠 충분한 공간이 이미 확보되어 있으며 문자열의 최종 길이가 함께 주어진다고 가정해도 된다(자바로 구현한다면 배열 안에서 작업 할 수 있도록 문자 배열(character array)을 이용하기 바란다)'''
# replace
import copy


def change_url(string):
    result = '%20'.join(string.split(' '))
    return result


print(change_url("This is a test sentense."))

# 문자열 끝에서 시작해 앞으로 읽어나가며 수정하는게 보통 쉽다
# 필요한 공백을 알아야 할지도 모른다 하나씩 세어 볼 수 있는가?
