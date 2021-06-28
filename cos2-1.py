'''#문제1
왼손 장갑의 제품 번호가 들어있는 리스트와 오른손 장갑의 제품 번호가 들어있는 리스트가 있습니다. 
제품 번호는 1부터 10 사이의 자연수입니다. 제품 번호가 같은 왼손장갑과 오른손 장갑을 합쳐 장갑 한 쌍을 만들 수 있습니다. 이때, 최대한 많은 쌍의 장갑을 만들면 최대 몇 쌍을 만들 수 있는지 구하려 합니다. 
이를 위해 다음과 같이 프로그램 구조를 작성했습니다. 

~~~
1. 왼손 장갑이 제품 번호별로 몇 개씩 있는지 개수를 셉니다.
2. 오른손 장갑이 제품 번호별로 몇 개씩 있는지 개수를 셉니다.
3. 각 제품 번호별로 최대한 많은 장갑 쌍을 만들면서 개수를 셉니다.
~~~

왼손 장갑의 제품 번호가 들어있는 리스트 left_gloves와 오른손 장갑의 제품 번호가 들어있는 
리스트 right_gloves가 매개변수로 주어질 때, 최대 몇 개의 장갑 쌍을 만들 수 있는지 return 하도록 
solution 함수를 작성하려 합니다. 이때, 위 구조를 참고하여 중복되는 부분은 func_a라는 함수로 작성했습니다. 
코드가 올바르게 동작할 수 있도록 빈칸을 알맞게 채워주세요.

---
##### 매개변수 설명
왼손 장갑의 제품 번호가 들어있는 리스트 left_gloves와 오른손 장갑의 제품 번호가 들어있는 리스트 right_gloves가 solution 함수의 매개변수로 주어집니다.

* left_gloves의 길이는 1 이상 100 이하입니다.
* left_gloves의 원소는 1 이상 10 이하의 자연수입니다.
* right_gloves의 길이는 1 이상 100 이하입니다.
* right_gloves의 원소는 1 이상 10 이하의 자연수입니다.

---
##### return 값 설명 
왼손과 오른손의 제품 번호가 같은 장갑 끼리 한 쌍을 만들 때, 최대 몇 개의 쌍을 만들 수 있는지 개수를 return 해주세요.

---
##### 예시

| left_gloves              | right_gloves                  | return |
|---------------------------|--------------------------------|--------|
| [2, 1, 2, 2, 4] | [1, 2, 2, 4, 4, 7] | 4      |

---
##### 예시 설명
예시 #1
왼손 장갑 : 1번 장갑 1개, 2번 장갑 3개, 4번 장갑 1개가 있습니다.
오른손 장갑 : 1번 장갑 1개, 2번 장갑 2개, 4번 장갑 2개, 7번 장갑 1개가 있습니다.

따라서 1번 장갑 한 쌍, 2번 장갑 두 쌍, 4번 장갑 한 쌍을 만들면 최대 4개의 장갑 쌍을 만들 수 있습니다.

max_product_number = 10

def func_a(gloves):
    counter = [0 for _ in range(max_product_number + 1)]
    for x in gloves:
        @@@
    return counter

def solution(left_gloves, right_gloves):
    left_counter = func_a(left_gloves)
    right_counter = func_a(right_gloves)
    
    total = 0
    for i in range(1, max_product_number + 1):
        total += min(left_counter[i], right_counter[i])
    return total

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
left_gloves = [2, 1, 2, 2, 4]
right_gloves = [1, 2, 2, 4, 4, 7]
ret = solution(left_gloves, right_gloves)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")'''



max_product_number = 10

def func_a(gloves):
    counter = [0 for _ in range(max_product_number + 1)]
    for x in gloves:
    	counter[x] += 1
    return counter

def solution(left_gloves, right_gloves):
    left_counter = func_a(left_gloves)
    right_counter = func_a(right_gloves)
    
    total = 0
    for i in range(1, max_product_number + 1):
        total += min(left_counter[i], right_counter[i])
    return total

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
left_gloves = [2, 1, 2, 2, 4]
right_gloves = [1, 2, 2, 4, 4, 7]
ret = solution(left_gloves, right_gloves)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

'''
정답
max_product_number = 10

def func_a(arr):
    max_product_number = 10
    counter = [0 for _ in range(max_product_number + 1)]
    for x in arr:
        counter[x] += 1 <---------------------------------------------------
    return counter

def solution(left_gloves, right_gloves):
    left_counter = func_a(left_gloves)
    right_counter = func_a(right_gloves)
    
    total = 0
    for i in range(1, max_product_number + 1):
        total += min(left_counter[i], right_counter[i])
    return total'''