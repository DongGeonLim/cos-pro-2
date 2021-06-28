'''#문제6
하루 동안 엘리베이터가 멈춘 층이 순서대로 들어있는 리스트가 있습니다. 이때, 엘리베이터의 총 이동거리를 구하려 합니다. 단, 층과 층 사이의 거리는 1입니다. 

예를 들어 리스트에 [1, 2, 5, 4, 2]가 들어있다면, 엘리베이터가 이동한 거리는 7입니다.
 
하루 동안 엘리베이터가 멈춰 선 층이 순서대로 들어있는 리스트 floors가 매개변수로 주어질 때, 엘리베이터의 총 이동 거리를 return 하도록 solution 함수를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.

---
#####매개변수 설명
하루 동안 엘리베이터가 멈춘 층이 순서대로 들어있는 리스트 floors가 solution 함수의 매개변수로 주어집니다.
* floors의 길이는 2 이상 100 이하입니다.
* floors의 원소는 1 이상 100 이하의 자연수이며, 인접한 두 원소의 값이 같은 경우는 주어지지 않습니다.
* floors의 첫 번째 원소는 엘리베이터의 처음 위치를 나타냅니다.

---
#####return 값 설명
엘리베이터의 총 이동 거리를 return 해주세요.

---
#####예시
| floors          | return |
|-----------------|--------|
| [1, 2, 5, 4, 2] | 7      |

#####예시 설명
엘리베이터는 처음에 1층에 있으며, 다음 순서대로 움직였습니다.

* 1층 - 2층 - 5층 - 4층 - 2층

층과 층사이의 거리는 1이므로, 엘리베이터가 이동한 거리는 다음과 같습니다.

* 1층 - 2층 (이동 거리 : 1)
* 2층 - 5층 (이동 거리 : 3)
* 5층 - 4층 (이동 거리 : 1)
* 4층 - 2층 (이동 거리 : 2)

따라서 총 이동 거리는 7입니다.

def solution(floors):
    dist = 0
    length = len(floors)
    for i in range(@@@):
        if @@@:
            dist += floors[i] - floors[i-1]
        else:
            dist += floors[i-1] - floors[i]
    return dist

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
floors = [1, 2, 5, 4, 2]
ret = solution(floors)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")'''

def solution(floors):
    dist = 0
    length = len(floors)
    for i in range(1, length):
        if floors[i] > floors[i-1]:
            dist += floors[i] - floors[i-1]
        else:
            dist += floors[i-1] - floors[i]
    return dist

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
floors = [1, 2, 5, 4, 2]
ret = solution(floors)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")


'''
정답
def solution(floors):
    dist = 0
    length = len(floors)
    for i in range(1, length):
        if floors[i] > floors[i-1]:
            dist += floors[i] - floors[i-1]
        else:
            dist += floors[i-1] - floors[i]
    return dist
'''
