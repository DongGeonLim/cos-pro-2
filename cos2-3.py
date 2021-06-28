'''#문제3
서로 다른 두 자연수 N과 M이 매개변수로 주어질 때, N부터 M까지의 자연수 중에서 짝수들의 제곱의 합을 
return 하도록 solution 함수를 완성해주세요.

---
#####매개변수 설명
두 자연수 N과 M이 solution 함수의 매개변수로 주어집니다.
* N과 M은 1 이상 1,000 이하의 자연수이며, N < M을 항상 만족합니다.

---
#####return 값 설명
N부터 M까지의 수 중에서 짝수인 수의 제곱의 합을 return 해주세요.

---
#####예시

| N | M | return |
|---|---|--------|
| 4 | 7 | 52     |

#####예시 설명
4부터 7까지의 자연수 중에서 짝수는 4와 6입니다.

* 4^2 + 6^2 = 16 + 36 = 52

따라서 52를 return 하면 됩니다.

#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(N, M):
    #여기에 코드를 작성해주세요.
    answer = 0
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
N = 4
M = 7
ret = solution(N, M)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")'''



#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(N, M):
    diff = M - N
    num = []
    for x in range(diff):
    	a = N + x
    	num.append(int(a))
    	print(num)
    for y in range(len(num)):
    	if int(num[y]) % 2 != 0:
    		num.remove(num[y])
    for z in range(len(num)):
    	num[z] = num[z]*num[z]
    for i in range(len(num)):
    	sum_num += num[z]
    return sum_num

# #아래는 테스트케이스 출력을 해보기 위한 코드입니다. 
N = 4
M = 7
ret = solution(N, M)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

'''
정답
def solution(N, M):
    total = 0
    for x in range(N, M + 1):
        if x % 2 == 0:
            total += x*x
    return total'''