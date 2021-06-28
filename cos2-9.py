'''#문제9
N명의 후보에 대해 투표한 결과가 들어있는 리스트가 있습니다. 예를 들어 5명의 후보에 대해 투표를 진행한 결과가 
[2, 5, 3, 4, 1, 5, 1, 5, 5, 3]이라면 순서대로 [2번, 5번, 3번, 4번, 1번, 5번, 1번, 5번, 5번, 3번] 후보에 투표했음을 나타냅니다. 
이때, 정확히 K 표를 받은 후보는 총 몇 명인지 구하려 합니다. 

예를 들어 K = 2일 때, 위 투표 결과에서 정확히 2표를 받은 후보는 1번, 3번 후보로, 총 2명입니다. 

투표 결과가 들어있는 리스트 votes, 후보의 수 N, 표의 개수 K가 매개변수로 주어질 때, 
K 표를 받은 후보는 몇 명인지 return 하도록 solution 함수를 작성했습니다. 
그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다. 
주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

---
#####매개변수 설명
투표 결과가 들어있는 리스트 votes, 후보의 수 N, 표의 개수 K가 solution 함수의 매개변수로 주어집니다.
* votes의 길이는 10 이상, 100 이하입니다.
* votes의 원소는 1 이상, 전체 후보의 수 N 이하의 자연수입니다.
* N은 3 이상 10 이하의 자연수입니다.
* K는 0 이상 100 이하의 정수입니다.

---
#####return 값 설명
K 표를 받은 후보는 몇 명인지 return 해주세요.

---
#####예시
| votes                          | N | K | return |
|--------------------------------|---|---|--------|
| [2, 5, 3, 4, 1, 5, 1, 5, 5, 3] | 5 | 2 | 2      |

#####예시 설명
각 후보가 받은 표는 다음과 같습니다.

* 1번 후보 : 2표
* 2번 후보 : 1표
* 3번 후보 : 2표
* 4번 후보 : 1표
* 5번 후보 : 4표

따라서 2표를 받은 후보는 1번, 3번 후보로 총 2명입니다.

def solution(votes, N, K):
    counter = [0 for _ in range(N + 1)]
    for x in votes:
        counter[x] += 1
    answer = -1
    for c in counter:
        if c == K:
            answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
votes = [2, 5, 3, 4, 1, 5, 1, 5, 5, 3]
N = 5
K = 2
ret = solution(votes, N, K)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")'''

def solution(votes, N, K):
    counter = [0 for _ in range(N + 1)]
    for x in votes:
        counter[x] += 1
    answer = 0
    for c in counter:
        if c == K:
            answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
votes = [2, 5, 3, 4, 1, 5, 1, 5, 5, 3]
N = 5
K = 2
ret = solution(votes, N, K)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")


'''
정답
def solution(votes, N, K):
    counter = [0 for _ in range(N + 1)]
    for x in votes:
        counter[x] += 1
    answer = 0
    for c in counter:
        if c == K:
            answer += 1
    return answer'''