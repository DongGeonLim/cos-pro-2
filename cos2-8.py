'''#문제8
자연수의 각 자릿수 중에서 소수는 몇 개인지 구하려 합니다. 즉, 자연수를 각 자릿수별로 나누었을 때, 2, 3, 5, 7이 몇 개 있는지 구하려 합니다.

예를 들어, 자연수가 29022531일 때, 각 자릿수 중 소수의 위치는 다음과 같습니다.

* `2`90`2``2``5``3`1

따라서 소수의 개수는 총 5개입니다.

자연수 number가 매개변수로 주어질 때, number의 각 자릿수 중 소수는 몇 개인지 return 하도록 solution 함수를 작성했습니다. 
그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다. 
주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

---
#####매개변수 설명
자연수 number가 solution 함수의 매개변수로 주어집니다.
* number는 1 이상 1,000,000,000 이하의 자연수입니다.

---
#####return 값 설명
number의 각 자릿수 중 소수는 몇 개인지 return 해주세요.

---
#####예시

| number   | return |
|----------|--------|
| 29022531 | 5      |

def solution(number):
    count = 0
    while number >= 0:
        n = number % 10
        if n == 2 or n == 3 or n == 5 or n == 7:
            count += 1
        number //= 10
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
number = 29022531
ret = solution(number)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")'''

def solution(number):
    count = 0
    while number > 0:
        n = number % 10
        if n == 2 or n == 3 or n == 5 or n == 7:
            count += 1
        number //= 10
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
#number = 29022531

number = 31135777
ret = solution(number)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

# 정답
# def solution(number):
#     count = 0
#     while number:
#         n = number % 10
#         if n == 2 or n == 3 or n == 5 or n == 7:
#             count += 1
#         number //= 10
#     return count
