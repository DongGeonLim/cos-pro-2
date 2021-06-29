# python programmerscospro2.py

'''
자연수가 담겨있는 n x 4 크기의 2차원 배열에서 k번째로 작은 수를 찾으려 합니다. 이때, n은 배열의 세로길이, 4는 배열의 가로길이입니다. 예를 들어 다음은 자연수가 담겨있는 4 x 4 크기의 2차원 배열입니다.

image

위 2차원 배열에서 가장 작은 수는 2입니다. 두 번째로 작은 수는 4, 세 번째로 작은 수는 5이며, 네 번째로 작은 수는 11입니다.

2차원 배열 arr와 k가 매개변수로 주어질 때, arr에서 k번째로 작은 수를 찾아 return 하도록 solution 함수를 완성해주세요.

매개변수 설명
2차원 배열 arr와 자연수 k가 solution 함수의 매개변수로 주어집니다.

arr는 n x 4 크기의 2차원 배열이며, n은 1 이상 20 이하입니다.
n은 arr의 세로길이이며, 가로길이는 항상 4입니다.
arr의 원소는 1 이상 1,000 이하의 자연수이며, 같은 수가 중복해서 들어있지 않습니다.
k는 1 이상 n x 4 이하의 자연수입니다.
return 값 설명
2차원 배열 arr에서 k번째로 작은 수를 찾아서 return 하도록 solution 함수를 작성해주세요.
'''
'''
def solution(arr, k):

    list1 = []
    for x in range(len(arr)):
        for y in range(4):

            list1.append(arr[x][y])

    list1.sort()
    answer = list1[k-1]
                  
    return answer
    
    디스이즈 나의 코드
    '''

def solution(arr, k):
    answer = 0
    answer = []
    for i in arr:
        answer += i
    print(answer)
    answer.sort()
    print(answer)
    return answer[k-1]


arr = [[5,12,4,31],[24,13,11,2],[43,44,19,26],[33,65,20,21]]
k = 4

ret = solution(arr,k)

print(ret)




'''

개구리가 일정한 간격으로 일렬로 놓여있는 징검다리를 건너려고 합니다.

image

징검다리에는 자연수가 적혀있으며, 개구리는 자신이 밟고 있는 징검다리에 적혀있는 숫자만큼 앞쪽으로 점프해야 합니다. 개구리는 현재 첫 번째 징검다리 위에 앉아있습니다.

징검다리에 적혀있는 숫자가 첫 번째부터 순서대로 들어있는 배열 stones가 매개변수로 주어질 때, 개구리가 징검다리를 모두 건너기 위해 필요한 점프 횟수를 return 하도록 solution 함수를 작성하려 합니다. 빈칸을 채워 전체 코드를 완성해주세요.

매개변수 설명
징검다리에 적힌 숫자가 첫 번째 징검다리부터 순서대로 들어있는 배열 stones가 solution 함수의 매개변수로 주어집니다.

stones 배열의 길이는 1 이상 100 이하입니다.
stones의 원소(돌에 적혀있는 숫자)는 1 이상 5 이하의 자연수입니다.
return값 설명
solution 함수는 개구리가 징검다리를 모두 건너기 위해 필요한 점프 횟수를 return 합니다.

예시
stones  result
[2,5,1,3,2,1]   3
예시 설명
예시 #1

6개의 징검다리에 순서대로 [2, 5, 1, 3, 2, 1]이 적혀있는 경우의 예시입니다.

image

위 그림에서 처음에 개구리는 가장 왼쪽에 있는 첫 번째 징검다리에 앉아있습니다.

첫 번째 징검다리에 2가 적혀있으므로 두 칸을 점프하여 세 번째 징검다리로 이동합니다.
세 번째 징검다리에는 1이 적혀 있으므로 한 칸을 점프하여 네 번째 징검다리로 이동합니다.
네 번째 징검다리에는 3이 적혀 있으므로 3칸을 점프하여 모든 징검다리를 건너게 됩니다.
위 예시에서 개구리는 총 3번 점프하여 모든 징검다리를 건넜습니다.


def solution(stones):
    cnt = 0
    current = 0
    n = len(stones)
    while current < len(stones):
        current += stones[current]
        cnt += 1
    return cnt

'''