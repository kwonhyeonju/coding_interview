
def solution(word):
    alcheck = 0
    for w in word:
        if alcheck & (1 << ord(w) - ord('a')):
            return False
        alcheck |= (1 << ord(w) - ord('a'))
    return True


print(ord('h') - ord('a'))
