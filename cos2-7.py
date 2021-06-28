'''#문제7
화씨온도(℉)를 섭씨온도(℃)로, 섭씨온도(℃)를 화씨온도(℉)로 바꾸려고 합니다. 두 온도 사이의 환산 공식은 다음과 같습니다.

~~~
환산공식
* 화씨온도(℉)에서 섭씨온도(℃)로 환산 : (화씨온도 - 32) ÷ 1.8 = 섭씨온도
* 섭씨온도(℃)에서 화씨온도(℉)로 환산 : (섭씨온도 x 1.8) + 32 = 화씨온도
~~~

현재 온도 value와 현재 단위 unit이 매개변수로 주어질 때, 환산한 온도의 정수 부분을 return 하도록 solution 함수를 작성했습니다. 
그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다. 
주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

---

#####매개변수 설명
현재 온도 value와 현재 단위 unit이 solution 함수의 매개변수로 주어집니다.
* unit은 화씨온도 "F"와 섭씨온도 "C" 둘 중 하나로 주어집니다.
  * unit이 "F"인 경우 value는 화씨온도(℉)를 나타냅니다.
  * unit이 "C"인 경우 value는 섭씨온도(℃)를 나타냅니다.
* value는 -460 이상 1,000 이하의 정수입니다.

---

##### return 값 설명
환산한 온도의 정수 부분을 return 해주세요.
* unit이 "F"인 경우에는 화씨온도(℉)에서 섭씨온도(℃)로 환산해주세요.
* unit이 "C"인 경우에는 섭씨온도(℃)에서 화씨온도(℉)로 환산해주세요.

---

#####예시 

| value | unit | return |
|-------|------|--------|
| 527   | "C"  | 980    |

#####예시 설명
unit이 "C" 이므로 주어진 value는 527℃를 나타냅니다. 이를 화씨온도(℉)로 환산하면 다음과 같습니다.
(섭씨온도 x 1.8) + 32 = (527 x 1.8) + 32 = 980.6

따라서 환산 결과는 980.6℉이며, 정수 부분만 return 하면 되므로 980을 return 하면 됩니다.

def solution(value, unit):
    converted = 0
    if unit == "C":
        value = value * 1.8 + 32
    if unit == "F":
        value = value - 32 / 1.8
    converted = int(value)
    return converted

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
value = 527
unit = "C"
ret = solution(value, unit)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")'''

def solution(value, unit):
    converted = 0
    if unit == "C":
        value = value * 1.8 + 32
    if unit == "F":
        value = (value - 32) / 1.8
    converted = int(value)
    return converted

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
value = 527
unit = "C"
ret = solution(value, unit)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")


'''
정답
def solution(value, unit):
    converted = 0
    if unit == "C":
        value = (value * 1.8) + 32
    if unit == "F":
        value = (value - 32) / 1.8
    converted = int(value)
    return converted
'''

a = 1 + 10 / 5

print(a)

b = 20

c = -b / 10 - 9

print(c)