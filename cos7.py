#문제7
'''
A 대학에서는 수준별 영어 강의를 제공하고 있습니다. 초급 영어 강의는 토익시험에서 
650점 이상 800점 미만의 성적을 취득한 학생만을 수강대상으로 하고 있습니다. 
초급 영어 강의에 수강신청한 사람이 10명일 때, 이 중에서 몇명이 수강 대상에 
해당하는지 확인하려합니다.

수강신청자들의 토익 성적이 들어있는 리스트 scores가 매개변수로 주어질 때, 
수강 대상자들의 인원수를 return 하도록 solution 함수를 작성했습니다. 
그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다. 
주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정해주세요.

---

#####매개변수 설명
수강신청자들의 토익 성적이 들어있는 리스트 scores가 solution 함수의 매개변수로 주어집니다.
* scores의 원소는 500 이상 990 이하의 정수입니다.
* scores의 길이는 10입니다.

---

#####return 값 설명
수강 대상자들의 인원수를 return 해주세요.

---

#####예시

| scores                                             | return |
|----------------------------------------------------|--------|
| [650, 722, 914, 558, 714, 803, 650, 679, 669, 800] | 6      |

#####예시 설명
|점수| 650 | 722 | 914 | 558 | 714 | 803 | 650 | 679 | 669 | 800 |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|수강 대상| O   | O   | X   | X   | O   | X   | O   | O   | O   | X   |

650점 이상 800점 미만의 성적을 취득한 학생이 수강대상이므로, 
800점을 취득한 학생은 수강대상이 아닙니다.
따라서, 6명이 수강 대상입니다.

def solution(scores):
    count = 0
    for s in scores:
        if 650 <= s or s < 800:
            count += 1
    return count

#The following is code to output testcase. The code below is correct and you shall correct solution function.
scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".") '''

def solution(scores):
    count = 0
    for s in scores:
        if 650 <= s < 800:
            count += 1
    return count

#The following is code to output testcase. The code below is correct and you shall correct solution function.
scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")

#정답
'''
def solution(scores):
    count = 0
    for i in range(len(scores)):
        if 650 <= scores[i] < 800:
            count += 1
    return count

#The following is code to output testcase. The code below is correct and you shall correct solution function.
scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")'''