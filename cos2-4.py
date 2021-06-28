#문제4
'''
단어들이 들어있는 리스트에서 길이가 5 이상인 단어를 리스트에 들어있는 순서대로 이어 붙이려 합니다.

예를 들어 리스트가 다음과 같은 경우

["my", "favorite", "color", "is", "violet"]

"favoritecolorviolet"을 만들면 됩니다.

단어들이 들어있는 리스트 words가 solution 함수의 매개변수로 주어질 때, 길이가 5 이상인 단어를 순서대로 이어 붙인 문자열을 return 하도록 solution 함수를 완성해주세요.

---
#####매개변수 설명
단어들이 들어있는 리스트 words가 solution 함수의 매개변수로 주어집니다.

* words의 길이는 1 이상 100 이하입니다.
* words에 들어있는 각 단어의 길이는 1 이상 10 이하이며, 알파벳 소문자로만 이루어져 있습니다.

---
#####return 값 설명
길이가 5 이상인 단어를 순서대로 이어 붙여 return 해주세요.
* 만약 return 할 문자열이 빈 문자열이면 "empty"를 return 해주세요.

---
#####예시

| words                                       | return                |
|---------------------------------------------|-----------------------|
| ["my", "favorite", "color", "is", "violet"] | "favoritecolorviolet" |
| ["yes", "i", "am"]                          | "empty"               |

#####예시 설명
예시 #1
길이가 5 이상인 단어는 "favorite", "color", "violet" 입니다. 이를 리스트에 들어있는 순서대로 이어 붙이면 "favoritecolorviolet"이 됩니다.

예시 #2
길이가 5 이상인 단어가 없으므로 "empty"를 return 하면 됩니다.

#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(words):
    #여기에 코드를 작성해주세요.
    answer = ''
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
words1 = ["my", "favorite", "color", "is", "violet"]
ret1 = solution(words1);

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

words2 = ["yes", "i", "am"]
ret2 = solution(words2);

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")'''




#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(words):
    answer = ''
    for x in words:
        if len(x) >= 5:
            answer += x
    if len(answer) == 0:
        answer += "empty"    
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
words1 = ["my", "favorite", "color", "is", "violet"]
ret1 = solution(words1);

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

words2 = ["yes", "i", "am"]
ret2 = solution(words2);

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")

'''
정답
def solution(words):
    answer = ""
    for w in words:
        if len(w) >= 5:
            answer += w
    if len(answer) < 1:
        answer = "empty"
    return answer '''

